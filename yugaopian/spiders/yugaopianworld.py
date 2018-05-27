# -*- coding: utf-8 -*-
import scrapy
from yugaopian.items import YugaopianItem


class YugaopianworldSpider(scrapy.Spider):
    name = 'yugaopianworld'
    allowed_domains = ['www.yugaopian.cn']
    start_urls = ['http://www.yugaopian.cn/allmovies']

    def parse(self, response):
        movlist = response.xpath("//div[@class='movlist']/ul/li")
        for result in movlist:
            item = YugaopianItem()
            item['name'] = result.xpath("./a/span[@class='item-title']/text()")[0].extract()
            item['pub_date'] = result.xpath("./a/span[@class='item-pubtime']/text()")[0].extract()
            item['movie_cover'] = result.xpath("./a/img/@src").extract()
            item['url'] = "%s%s" % ("https://www.yugaopian.cn", result.xpath("./a/@href")[0].extract())
            item['img_urls'] = item['movie_cover']
            request = scrapy.Request(url=item['url'], meta={"key": item}, callback=self.parse_detail)

            yield request

            if response.xpath("//p[@class='page-nav']/a[text()='下一页']/@href"):
                next_url = "%s%s" % (
                    "https://www.yugaopian.cn",
                    response.xpath("//p[@class='page-nav']/a[text()='下一页']/@href")[0].extract())
                yield scrapy.Request(next_url, callback=self.parse)

        # pass

    def parse_detail(self, response):
        item = response.meta['key']
        #   // div[ @class ='movie-title-detail'] / p / span[@ class ="detail-title" and text()="导演："] / following-sibling:: a[1] / text()
        item['director'] = response.xpath(
            '//div[@class="movie-title-detail"]/p/span[@class="detail-title" and text()="导演："]/following-sibling::a[1]/text()')[0].extract()
        item['actor'] = response.xpath(
            '//div[@class="movie-title-detail"]/p/span[@class="detail-title" and text()="主演："]/following-sibling::a/text()')[0].extract()
        item['desc'] = response.xpath(
            '//div[@class="movie-title-detail"]/p/span[@class="detail-title" and text()="剧情："]/following-sibling::text()')[0].extract()
        yield item
