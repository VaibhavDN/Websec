# -*- coding: utf-8 -*-
import scrapy
import request
import response
from ..items import Website2Item
class Tech2Spider(scrapy.Spider):
    name = 'tech2'
    start_urls = ['https://www.technologyreview.com/']

    def parse(self, response):
        items=Website2Item()
        text=response.css('.jsx-2366629197,.jsx-2366629197, .feedUnitWrapper, .headLink').css('::text').extract()
        items['text']=text
        yield items
