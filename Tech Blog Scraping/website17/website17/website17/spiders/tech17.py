# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website17Item
class Tech5Spider(scrapy.Spider):
    name = 'tech17'
    start_urls = ['https://fossbytes.com/']

    def parse(self, response):
    	items=Website17Item()
    	text=response.css('a').css('::text').extract()
    	items['text']=text
    	yield items