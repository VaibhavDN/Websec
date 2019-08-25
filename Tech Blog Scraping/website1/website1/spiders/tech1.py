# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website1Item


class Tech1Spider(scrapy.Spider):
    name = 'tech1'
    start_urls = ['https://www.techmeme.com/190824/p10#a190824p10']

    def parse(self, response):
    	items=Website1Item()
    	text=response.css('.ourh').css('::text').extract()
    	items['text']=text
    	yield items
 

