# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website3Item



class Tech3Spider(scrapy.Spider):
    name = 'tech3'
    start_urls = ['https://readwrite.com/']
    def parse(self, response):
    	items=Website3Item()
    	text=response.css('.col-md-9 .entry-title a').css('::text').extract()
    	items['text']=text
    	yield items
       
