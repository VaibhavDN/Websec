# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website7Item
class Tech5Spider(scrapy.Spider):
    name = 'enter7'
    start_urls = ['http://collider.com/']

    def parse(self, response):
    	items=Website7Item()
    	text=response.css('#slidertitle , h2').css('::text').extract()
    	items['text']=text
    	yield items