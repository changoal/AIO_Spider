# -*- coding: utf-8 -*-

import json
import os

import scrapy
from spider.items import SpiderItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true']

    def parse(self, response):
        res = json.loads(response.text)
        for data in res['data']:
            target = data['target']
            if target:
                print(target)
                item = SpiderItem()
                item['extra'] = data
                item['title'] = target['title']
                item['author'] = target['author']['name']
                item['link'] = target['url']
                item['source'] = '知乎'
                item['pub_time'] = target['created']
                item['desc'] = target['excerpt']
                yield item


def write(data):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zhihu_data.json')
    print(file)
    print(os.path.abspath(file))
    with open(file, 'w') as f:
        f.write(data)
