# -*- coding: utf-8 -*-
import scrapy
from ..items import ReviewcrawlerItem
import csv
#from scrapy.crawler import CrawlerProcess


with open('/home/baka/SentiMovie/search.csv','r') as f:
    reader=csv.reader(f)
    data=[row for row in reader]
    #print(data[1])

q = ''.join(data[1])

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
        for link in links[:5]:
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
         
         """yielding from here would result in format mismatch"""
         review_link=response.css(".review_container>div>div>p>a::attr(href)").extract()
         for link in review_link:
             yield scrapy.Request(response.urljoin(link),callback=self.extract_reviews,meta={'title':title,
                                  'overview':overview,'language':language,'runtime':runtime,'budget':budget,
                                  'revenue':revenue,'genres':genres,'released_date':released_date,
                                  'cast_members':cast_members,'crew_members':crew_members})
         
    def extract_reviews(self,response):
        title=response.meta['title']
        overview=response.meta['overview']
        language=response.meta['language']
        runtime=response.meta['runtime']
        budget=response.meta['budget']
        revenue=response.meta['revenue']
        genres=response.meta['genres']
        released_date=response.meta['released_date']
        cast_members=response.meta['cast_members']
        crew_members=response.meta['crew_members']
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
        reviews=response.css(".card>div>div>h3::text,.card>div>div>div>h3>a::text,.card>div>p::text").extract()
        print(reviews)
        items['reviews']=reviews
        yield items

        
      
        
        
# =============================================================================
# process=CrawlerProcess({
#         'FEED_FORMAT':'csv',
#         'FEED_URI':'items.csv'
# })
# 
# process.crawl(reviewspider)
# process.start()
#             
# =============================================================================
        
  
        