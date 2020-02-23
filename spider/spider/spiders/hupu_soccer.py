# -*- coding: utf-8 -*-

import json

import scrapy
from spider.items import SpiderItem


class SMZDMSpider(scrapy.Spider):
    name = 'hupu_soccer'
    allowed_domains = ['hupu.com']
    start_urls = ['https://soccer.hupu.com/api/v1/fifa']

    def parse(self, response):
        res = json.loads(response.text)
        for data in res['data']:
            item = SpiderItem()
            if data['hasImg']:
                item['image'] = data['img']
            item['title'] = data['title']
            item['link'] = data['url']
            item['tag'] = data['like']
            yield item
