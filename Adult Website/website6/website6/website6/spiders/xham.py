# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website6Item


class XhamSpider(scrapy.Spider):
    name = 'xham1'
    start_urls = ['https://www.porntube.com/']

    def parse(self, response):
    	item=Website6Item()
    	text=response.css('.info').css('::text').extract()
    	item['text']=text
    	yield item
       