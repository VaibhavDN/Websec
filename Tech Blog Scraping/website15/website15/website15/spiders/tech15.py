# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website15Item
class Tech5Spider(scrapy.Spider):
    name = 'tech15'
    start_urls = ['https://www.techspot.com/']

    def parse(self, response):
    	items=Website15Item()
    	text=response.css('h2').css('::text').extract()
    	items['text']=text
    	yield items