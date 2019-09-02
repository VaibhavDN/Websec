# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website2Item


class XhamSpider(scrapy.Spider):
    name = 'bolly'
    start_urls = ['https://www.filmykeeday.com/action-movies-of-bollywood/']

    def parse(self, response):
    	item=Website2Item()
    	text=response.css('strong , p').css('::text').extract()
    	item['text']=text
    	yield item
       