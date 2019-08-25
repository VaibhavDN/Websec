# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website10Item
class Tech5Spider(scrapy.Spider):
    name = 'enter10'
    start_urls = ['https://www.boxofficemojo.com/']

    def parse(self, response):
    	items=Website10Item()
    	text=response.css('#col3 td , font , p , #storyspc a').css('::text').extract()
    	items['text']=text
    	yield items