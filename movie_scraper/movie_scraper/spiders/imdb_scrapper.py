# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import MovieScraperItem


class ImdbScrapperSpider(scrapy.Spider):
    name = 'imdb_scrapper'
    allowed_domains = ['imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title?count=100&title_type=feature&ref_=nv_wl_img_2'
        ]

    def parse(self, response):
        
        movie_res = []
        movies = response.css(".mode-advanced")
        for movie in movies:
            movie_name = movie.css('.lister-item-header a').css('::text').extract()
            movie_rating = movie.css('.ratings-imdb-rating strong').css('::text').extract()
            movie_cast = movie.css('.lister-item-content .ghost~ a').css('::text').extract()
            movie_res.append({
                "movie_name": movie_name,
                "movie_rating": movie_rating,
                "movie_cast": movie_cast,
            })
        movie_res = json.dumps(movie_res, indent=4)
        print(movie_res)

        
