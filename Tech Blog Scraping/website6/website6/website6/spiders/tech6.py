# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website6Item


class Tech5Spider(scrapy.Spider):
    name = 'tech6'
    start_urls = ['https://www.vox.com/recode']

    def parse(self, response):
    	items=Website6Item()
    	text=response.css('.c-entry-box--compact__title a').css('::text').extract()
    	items['text']=text
    	yield items
