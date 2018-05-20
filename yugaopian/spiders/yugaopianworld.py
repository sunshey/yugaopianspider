# -*- coding: utf-8 -*-
import scrapy


class YugaopianworldSpider(scrapy.Spider):
    name = 'yugaopianworld'
    allowed_domains = ['www.yugaopian.cn']
    start_urls = ['http://www.yugaopian.cn/allmovies']

    def parse(self, response):
        pass
