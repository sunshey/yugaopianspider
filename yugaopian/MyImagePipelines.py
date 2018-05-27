# -*- coding:utf-8 -*-

from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem


class MyImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['img_urls']:
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
