# -*- coding: utf-8 -*-

import json
import time

import scrapy
from spider.items import SpiderItem


class SMZDMSpider(scrapy.Spider):
    name = 'smzdm_article'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://post.smzdm.com/rank/json_more/?unit=1']

    def parse(self, response):
        res = json.loads(response.text)
        datas = res['data']
        for data in datas:
            # 有时候会出现 [] 的情况
            if data is dict:
                item = SpiderItem()
                item['extra'] = data
                item['title'] = data['title']
                item['tag'] = data['up_count']
                item['link'] = data['article_url']
                item['author'] = data['nickname']
                item['image'] = data['pic_url']
                pub_date = data['publish_time']
                d = time.mktime(time.strptime(pub_date, "%Y-%m-%d %H:%M:%S"))
                item['pub_time'] = int(d) * 1000
                item['desc'] = data['content']
                item['source'] = '什么值得买'
                item['channel'] = '好文'
                yield item
