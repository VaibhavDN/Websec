# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website10Item
class Tech5Spider(scrapy.Spider):
    name = 'tech10'
    start_urls = ['https://www.reuters.com/news/technology']

    def parse(self, response):
    	items=Website10Item()
    	text=response.css('.story-content').css('::text').extract()
    	items['text']=text
    	yield items