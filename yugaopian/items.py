# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YugaopianItem(scrapy.Item):
    name = scrapy.Field()
    pub_date = scrapy.Field()
    movie_cover = scrapy.Field()
