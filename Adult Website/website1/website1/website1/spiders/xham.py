# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website1Item


class XhamSpider(scrapy.Spider):
    name = 'xham'
    start_urls = ['https://xhamster.com/']

    def parse(self, response):
    	item=Website1Item()
    	text=response.css('.video-thumb-info__name').css('::text').extract()
    	item['text']=text
    	yield item
       
