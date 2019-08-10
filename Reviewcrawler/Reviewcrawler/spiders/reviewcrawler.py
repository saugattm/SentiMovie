# -*- coding: utf-8 -*-
import scrapy
from ..items import ReviewcrawlerItem
class reviewspider(scrapy.Spider):
    name='reviewcrawler'
    start_urls =["https://www.themoviedb.org/"]    

    def parse(self,response):
        return scrapy.FormRequest.from_response(
                response,
                formxpath="//*[(@id = 'search_v4')]",
                formdata={
                        "query":"rocketman",
                        "language":"en-US"},
                callback=self.after_results
            )
    def after_results(self,response):
        nameresults=response.css(".title::text").extract()
        overview=response.css(".overview::text").extract()
        results=zip(nameresults,overview)
        for n,o in results:
            print(n+"==>info----->"+o)
            print("\n")
        link= response.css('.title.result::attr(href)').extract()
# =============================================================================
#         items=ReviewcrawlerItem()
#         for i in range(0,len(link)):
#             items['title']=nameresults[i]
#             items['overview']=overview[i]
#             items['link']=link[i]
#             yield items
# =============================================================================
       # i=int(input("enter a number"))
        yield scrapy.Request(response.urljoin(link[0]),callback= self.parse_data)
            
    def parse_data(self,response):
        ctitle= response.css(".profile p::text").extract()
        cname=response.css(".profile p>a::text").extract()
        review=response.css(".teaser p::text").extract()
        items =ReviewcrawlerItem()
        items['ctitle']=ctitle
        items['cname']=cname
        items['review']=review
        
        yield items 
        
        
  
        