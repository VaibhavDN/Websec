# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website1Item


class XhamSpider(scrapy.Spider):
    name = 'bolly'
    start_urls = ['https://www.highheelconfidential.com/page/10/']

    def parse(self, response):
    	item=Website1Item()
    	text=response.css('.article__inner p').css('::text').extract()
    	item['text']=text
    	yield item
       