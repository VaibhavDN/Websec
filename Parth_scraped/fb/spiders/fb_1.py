# -*- coding: utf-8 -*-
import scrapy
from ..items import FbItem


class Fb1Spider(scrapy.Spider):
    name = 'facebook'
    
    start_urls = ['https://www.facebook.com/parth.bhatt.146']

    def parse(self, response):
        items=FbItem()
        content=respose.css('::text').extract()
        items['text_fb']=text_fb
        yield items
     
      
