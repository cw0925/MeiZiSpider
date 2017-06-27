#!/usr/bin/python
# -*- coding:utf-8 -*-
import scrapy
from MeiZi.items import MeiziItem

class MeiZiSpider(scrapy.Spider):
    name = 'MeiZi'
    start_urls = ['http://www.meizitu.com/a/xiaoqingxin.htm','http://www.meizitu.com/a/nvshen.html']
# 作者
    def parse(self, response):
        # sel = scrapy.Selector(response)
        for item in response.xpath('//ul[@class="wp-list clearfix"]/li'):
            model = MeiziItem()
            # 标题
            title = item.xpath(
                './div[@class="con"]/h3/a/b/text()').extract()
            model["title"] = title
            # 图片
            url = item.xpath('./div[@class="con"]/div[@class="pic"]/a/img/@src').extract()
            model["img"] = url
            # 点击图片的url
            nexturl = item.xpath('./div[@class="con"]/div[@class="pic"]/a/@href').extract()
            model["nexturl"] = nexturl
            print(nexturl)
            yield model