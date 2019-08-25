# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website14Item
class Tech5Spider(scrapy.Spider):
    name = 'tech14'
    start_urls = ['https://abcnews.go.com/Technology']

    def parse(self, response):
    	items=Website14Item()
    	text=response.css('#uf-manager-content h1').css('::text').extract()
    	items['text']=text
    	yield items