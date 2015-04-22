# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    user=scrapy.Field()
    timestamp=scrapy.Field()
    topic=scrapy.Field()
    text=scrapy.Field()

class SiteItem(scrapy.Item):
    body=scrapy.Field()
    topic=scrapy.Field()


