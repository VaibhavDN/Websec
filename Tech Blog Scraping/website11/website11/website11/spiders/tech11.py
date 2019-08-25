# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website11Item
class Tech5Spider(scrapy.Spider):
    name = 'tech11'
    start_urls = ['https://www.express.co.uk/life-style/science-technology']

    def parse(self, response):
    	items=Website11Item()
    	text=response.css('h4').css('::text').extract()
    	items['text']=text
    	yield items