# -*- coding: utf-8 -*-

import json
import time

import scrapy
from spider.items import SpiderItem


class SMZDMSpider(scrapy.Spider):
    name = 'smzdm_price'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/top/json_more?rank_type=pinlei&rank_id=11&hour=24']

    def parse(self, response):
        res = json.loads(response.text)
        data = res['data']
        list = data['list']
        for datas in list:
            for data in datas:
                # 有时候会出现 [] 的情况
                if data is dict:
                    item = SpiderItem()
                    item['extra'] = data
                    item['title'] = data['article_title']
                    item['tag'] = data['sort']
                    item['link'] = data['article_url']
                    item['image'] = data['article_pic']
                    pub_date = data['article_pubdate']
                    d = time.mktime(time.strptime(pub_date, "%Y-%m-%d %H:%M:%S"))
                    item['pub_time'] = int(d) * 1000
                    item['desc'] = data['article_price']
                    item['source'] = '什么值得买'
                    item['channel'] = '好价'
                    yield item
