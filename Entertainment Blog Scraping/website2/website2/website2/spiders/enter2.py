# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website2Item
class Tech5Spider(scrapy.Spider):
    name = 'enter2'
    start_urls = ['https://movieweb.com/']

    def parse(self, response):
    	items=Website2Item()
    	text=response.css('.news-item-summary , .news-item-title a').css('::text').extract()
    	items['text']=text
    	yield items