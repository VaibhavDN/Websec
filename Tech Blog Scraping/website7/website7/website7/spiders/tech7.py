# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website7Item


class Tech5Spider(scrapy.Spider):
    name = 'tech7'
    start_urls = ['https://www.nytimes.com/section/technology']

    def parse(self, response):
    	items=Website7Item()
    	text=response.css('.e1xfvim30 , .e1xdw5350 a , .e1xdw5352 a').css('::text').extract()
    	items['text']=text
    	yield items