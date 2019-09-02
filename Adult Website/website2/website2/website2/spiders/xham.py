# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website2Item


class XhamSpider(scrapy.Spider):
    name = 'xham1'
    start_urls = ['https://www.pornhub.com/']

    def parse(self, response):
    	item=Website2Item()
    	text=response.css('.clearfix .title').css('::text').extract()
    	item['text']=text
    	yield item
       