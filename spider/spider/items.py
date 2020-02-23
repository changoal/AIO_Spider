# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 链接地址
    link = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    # 图片链接
    image = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 原数据
    extra = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 栏目
    channel = scrapy.Field()
