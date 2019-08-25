# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website20Item
class Tech5Spider(scrapy.Spider):
    name = 'tech20'
    start_urls = ['https://www.macworld.com/']

    def parse(self, response):
    	items=Website20Item()
    	text=response.css('#home-main-primary a , h2').css('::text').extract()
    	items['text']=text
    	yield items