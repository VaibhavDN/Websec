# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website6Item
class Tech5Spider(scrapy.Spider):
    name = 'enter6'
    start_urls = ['https://www.rogerebert.com/']

    def parse(self, response):
    	items=Website6Item()
    	text=response.css('#advallyAdhesionUnitClose img , h4 , p').css('::text').extract()
    	items['text']=text
    	yield items