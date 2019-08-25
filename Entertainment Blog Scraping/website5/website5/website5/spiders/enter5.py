# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website5Item
class Tech5Spider(scrapy.Spider):
    name = 'enter5'
    start_urls = ['https://www.comingsoon.net/']

    def parse(self, response):
    	items=Website5Item()
    	text=response.css('.listed-article-content :nth-child(1)').css('::text').extract()
    	items['text']=text
    	yield items