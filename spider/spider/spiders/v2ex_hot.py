# -*- coding: utf-8 -*-

import json

import scrapy
from spider.items import SpiderItem


class ZhihuSpider(scrapy.Spider):
    name = 'v2ex_hot'
    allowed_domains = ['v2ex.com']
    start_urls = ['https://www.v2ex.com/api/topics/hot.json']

    def parse(self, response):
        res = json.loads(response.text)
        for data in res:
            item = SpiderItem()
            item['extra'] = data
            item['title'] = data['title']
            item['author'] = data['member']['username']
            item['link'] = data['url']
            item['source'] = 'v2ex'
            item['pub_time'] = data['created']
            item['desc'] = data['content']
            yield item
