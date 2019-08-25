# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website19Item
class Tech5Spider(scrapy.Spider):
    name = 'tech19'
    start_urls = ['https://hackaday.com/blog/']

    def parse(self, response):
    	items=Website19Item()
    	text=response.css('.entry-content').css('::text').extract()
    	items['text']=text
    	yield items