# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewcrawlerItem(scrapy.Item):
    title=scrapy.Field()
    overview=scrapy.Field()
    language=scrapy.Field()
    runtime=scrapy.Field()
    budget=scrapy.Field()
    revenue=scrapy.Field()
    genres=scrapy.Field()
    released_date=scrapy.Field()
    cast_members=scrapy.Field()
    crew_members=scrapy.Field()
    reviews=scrapy.Field()
    
