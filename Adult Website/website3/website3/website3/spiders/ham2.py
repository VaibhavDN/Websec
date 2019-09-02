# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website3Item


class XhamSpider(scrapy.Spider):
    name = 'xham1'
    start_urls = ['https://www.indianpornvideos2.com/?filter=most-viewed']

    def parse(self, response):
    	item=Website3Item()
    	text=response.css('.title').css('::text').extract()
    	item['text']=text
    	yield item
       