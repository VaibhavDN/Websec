# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website8Item


class Tech5Spider(scrapy.Spider):
    name = 'tech8'
    start_urls = ['https://medium.com/@asiaainews']

    def parse(self, response):
    	items=Website8Item()
    	text=response.css('.gy').css('::text').extract()
    	items['text']=text
    	yield items