# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website5Item


class XhamSpider(scrapy.Spider):
    name = 'xham1'
    start_urls = ['https://www.redtube.com/tag/couple']

    def parse(self, response):
    	item=Website5Item()
    	text=response.css('.video_title').css('::text').extract()
    	item['text']=text
    	yield item
       