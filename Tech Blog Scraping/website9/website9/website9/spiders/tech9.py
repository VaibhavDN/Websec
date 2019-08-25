# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website9Item


class Tech5Spider(scrapy.Spider):
    name = 'tech9'
    start_urls = ['https://www.washingtonpost.com/business/technology/?noredirect=on']

    def parse(self, response):
    	items=Website9Item()
    	text=response.css('p').css('::text').extract()
    	items['text']=text
    	yield items