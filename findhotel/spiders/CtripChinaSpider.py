# -*- coding:utf-8 -*-
"""
    :author: Albert Li
    :time: 2019/11/17 15:12
"""
import scrapy


class CtripChinaSpider(scrapy.Spider):
    """携程国内酒店爬虫"""
    name = "CtripChina"
    # 允许爬取的范围，防止爬虫爬到了别的网站
    allowed_domains = ['hotels.ctrip.com']
    # 开始爬取的地址，下载中间件提取网页数据
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        """数据解析方法，接收下载中间件传递过来的响应"""
        pass
