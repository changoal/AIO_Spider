# -*- coding: utf-8 -*-

import json

import scrapy
from spider.items import SpiderItem


class ShuZiWeiBaSpider(scrapy.Spider):
    name = 'shuziweiba'
    allowed_domains = ['dgtle.com/']
    start_urls = ['https://www.dgtle.com/article/getList/0?page=1&pushed=1&last_id=0']

    def parse(self, response):
        res = json.loads(response.text)
        data = res['data']
        data_list = data['dataList']
        for data in data_list:
            item = SpiderItem()
            item['extra'] = data
            item['title'] = data['title']
            item['author'] = data['user_name']
            aid = data['id']
            item['link'] = 'https://www.dgtle.com/article-{}-1.html'.format(aid)
            item['image'] = data['cover']
            item['source'] = '数字尾巴'
            item['pub_time'] = data['created_at']
            item['desc'] = data['content']

            yield item
