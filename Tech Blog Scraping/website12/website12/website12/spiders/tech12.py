# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website12Item
class Tech5Spider(scrapy.Spider):
    name = 'tech12'
    start_urls = ['https://www.howtogeek.com/']

    def parse(self, response):
    	items=Website12Item()
    	text=response.css('a , #post-0 .entry-title').css('::text').extract()
    	items['text']=text
    	yield items