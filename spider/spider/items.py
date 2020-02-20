# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    source = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    extra = scrapy.Field()
    tag = scrapy.Field()

