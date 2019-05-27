# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieScraperItem


class ImdbScrapperSpider(scrapy.Spider):
    name = 'imdb_scrapper'
    allowed_domains = ['imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title?count=100&title_type=feature&ref_=nv_wl_img_2'
        ]

    def parse(self, response):
        items = MovieScraperItem()

        movie_name = response.css('.lister-item-header a').css('::text').extract()
        movie_rating = response.css('.ratings-imdb-rating strong').css('::text').extract()
        movie_cast = response.css('.lister-item-content .ghost~ a').css('::text').extract()

        items['movie_name'] = movie_name
        items['movie_rating'] = movie_rating
        items['movie_cast'] = movie_cast

        yield items
