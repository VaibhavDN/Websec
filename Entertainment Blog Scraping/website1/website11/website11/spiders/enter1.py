# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website11Item
class Tech5Spider(scrapy.Spider):
    name = 'enter1'
    start_urls = ['https://lwlies.com/']

    def parse(self, response):
    	items=Website11Item()
    	text=response.css('.excerpt , a').css('::text').extract()
    	items['text']=text
    	yield items