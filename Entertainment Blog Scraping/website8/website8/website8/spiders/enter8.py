# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website8Item
class Tech5Spider(scrapy.Spider):
    name = 'enter8'
    start_urls = ['https://geektyrant.com/']

    def parse(self, response):
    	items=Website8Item()
    	text=response.css('.title a').css('::text').extract()
    	items['text']=text
    	yield items