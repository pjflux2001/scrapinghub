# -*- coding: utf-8 -*-
import scrapy


class BooksPySpider(scrapy.Spider):
    name = 'books.py'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        self.log('I just visited :' + response.url)
        for book in response.css('ol.row > li > article > h3 > a::text').extract():
            yield {
                'title': response.css('ol.row > li > article > h3 > a::text').extract_first(),
                'link': response.urljoin(response.css('ol.row > li > article > h3 > a::attr(href)').extract_first())
            }
