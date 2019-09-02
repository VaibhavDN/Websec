# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import WebsiteItem


class XhamSpider(scrapy.Spider):
    name = 'xham1'
    start_urls = ['https://www.xnxx.com/']

    def parse(self, response):
    	item=WebsiteItem()
    	text=response.css('#content-thumbs a').css('::text').extract()
    	item['text']=text
    	yield item
       