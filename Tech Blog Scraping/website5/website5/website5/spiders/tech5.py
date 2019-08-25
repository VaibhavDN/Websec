# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website5Item


class Tech5Spider(scrapy.Spider):
    name = 'tech5'
    start_urls = ['https://venturebeat.com/']

    def parse(self, response):
    	items=Website5Item()
    	text=response.css('.article-title a').css('::text').extract()
    	items['text']=text
    	yield items
