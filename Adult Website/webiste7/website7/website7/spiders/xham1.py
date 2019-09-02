# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website7Item


class XhamSpider(scrapy.Spider):
    name = 'xham1'
    start_urls = ['https://www.indianpornvideos2.com/category/ass/page4']

    def parse(self, response):
    	item=Website7Item()
    	text=response.css('.title').css('::text').extract()
    	item['text']=text
    	yield item
       