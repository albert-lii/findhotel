# -*- coding:utf-8 -*-
"""
    :author: Albert Li
    :time: 2019/11/17 15:14
"""
import scrapy


class CtripInterSpider(scrapy.Spider):
    """携程国际酒店爬虫"""
    name = "CtripInter"

    def parse(self, response):
        pass
