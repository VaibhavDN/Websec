# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website16Item
class Tech5Spider(scrapy.Spider):
    name = 'tech16'
    start_urls = ['https://bgr.com/tech/']

    def parse(self, response):
    	items=Website16Item()
    	text=response.css('.link-channel-tech').css('::text').extract()
    	items['text']=text
    	yield items