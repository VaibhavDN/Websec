# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website13Item
class Tech5Spider(scrapy.Spider):
    name = 'tech13'
    start_urls = ['https://www.digitaltrends.com/cool-tech/']

    def parse(self, response):
    	items=Website13Item()
    	text=response.css('.dt-clamp-3 a').css('::text').extract()
    	items['text']=text
    	yield items