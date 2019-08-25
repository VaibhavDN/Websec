# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website9Item
class Tech5Spider(scrapy.Spider):
    name = 'enter9'
    start_urls = ['https://www.reddit.com/r/movies/']

    def parse(self, response):
    	items=Website9Item()
    	text=response.css('._1qeIAgB0cPwnLhDF9XSiJM , ._eYtD2XCVieq6emjKBH3m , ._12FoOEddL7j_RgMQN0SNeU , .t3_ctqebq').css('::text').extract()
    	items['text']=text
    	yield items