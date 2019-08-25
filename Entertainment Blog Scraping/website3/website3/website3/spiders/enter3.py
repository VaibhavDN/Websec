# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website3Item
class Tech5Spider(scrapy.Spider):
    name = 'enter3'
    start_urls = ['https://www.cinemablend.com/']

    def parse(self, response):
    	items=Website3Item()
    	text=response.css('.title h2').css('::text').extract()
    	items['text']=text
    	yield items