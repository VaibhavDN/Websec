# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website18Item
class Tech5Spider(scrapy.Spider):
    name = 'tech18'
    start_urls = ['https://thenextweb.com/section/tech/']

    def parse(self, response):
    	items=Website18Item()
    	text=response.css('.story-title a , .cover-title a').css('::text').extract()
    	items['text']=text
    	yield items