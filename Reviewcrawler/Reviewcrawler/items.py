# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewcrawlerItem(scrapy.Item):
# =============================================================================
#     title=scrapy.Field()
#     overview=scrapy.Field()
#     link=scrapy.Field()
# =============================================================================
    cname=scrapy.Field()
    ctitle=scrapy.Field()
    review=scrapy.Field()
    
