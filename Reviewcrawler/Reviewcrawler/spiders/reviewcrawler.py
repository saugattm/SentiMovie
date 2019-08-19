# -*- coding: utf-8 -*-
import scrapy
from ..items import ReviewcrawlerItem

#from scrapy.crawler import CrawlerProcess
q="Avengers"

class reviewspider(scrapy.Spider):
    name='reviewcrawler'
    start_urls =["https://www.themoviedb.org/"]    

    def parse(self,response):
        return scrapy.FormRequest.from_response(
                response,
                formxpath="//*[(@id = 'search_v4')]",
                formdata={
                        "query":q,
                        "language":"en-US"
                        },
                callback=self.after_results
            )
    def after_results(self,response):
        links= response.css('.title.result::attr(href)').extract() 
        for link in links[:7]:
            #print(link)
            yield scrapy.Request(response.urljoin(link),callback= self.parse_data)
            
    def parse_data(self,response):
        

         title=response.css('.title>span>a>h2::text').extract()
         #print(title)
 
         overview=response.css(".overview p::text").extract()
         #print (overview)
         
         language= response.css(".releases+ p::text").extract()
         #print(language)
         
         runtime=response.css("p:nth-child(7)::text").extract()
         #print(runtime)
         
         budget=response.css("p:nth-child(8)::text").extract()
         #print(budget)
         
         revenue=response.css("p:nth-child(9)::text").extract()
         #print(revenue)
         
         genres=response.css(".genres>ul>li>a::text").extract()
         #print(genres)
         
         released= response.css(".releases li::text").extract()
         
         """l=['\n        ', '\n        July  7, 2017', '\n        ', '\n        ', '\n      ', '\n        ', '\n        October 17, 2017', '\n        ', '\n        ', '\n      '] cleaning this type of date"""
         
         released_date=[x.replace(' ','').replace('\n','') for x in released]
         released_date=[x for x in released_date if x]
         #print(released_date)
         
         cast_members=response.css("#media_v4 .character::text , #media_v4 .people a::text").extract()
         cast_members=[x.replace(' ','').replace('\n','') for x in cast_members]
         cast_members=[x for x in cast_members if x]      
         #print(cast_members)               
         
         crew_members=response.css('.profile p::text,.profile p>a::text').extract()
         #print(crew_members)
         
         items =ReviewcrawlerItem()
         
         items['title']=title
         items['overview']=overview
         items['language']=language
         items['runtime']=runtime
         items['budget']=budget
         items['revenue']=revenue
         items['genres']=genres
         items['released_date']=released_date
         items['cast_members']=cast_members
         items['crew_members']=crew_members
         yield items
         review_link=response.css(".review_container>div>div>p>a::attr(href)").extract()
         for link in review_link:
             yield scrapy.Request(response.urljoin(link),callback=self.extract_reviews)
         
    def extract_reviews(self,response):
        reviews=response.css(".teaser p::text").extract()
        items =ReviewcrawlerItem()
        items['reviews']=reviews
        yield items
        #print(reviews)
        
        
        
        
# =============================================================================
# process=CrawlerProcess({
#         'FEED_FORMAT':'csv',
#         'FEED_URI':'items.csv'
# })
# 
# process.crawl(reviewspider)
# process.start()
# =============================================================================
            
        
  
        