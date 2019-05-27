# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieScraperItem


class ImdbScraperSpider(scrapy.Spider):
    name = 'imdb_scraper'
    allowed_domains = ['imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title?count=100&title_type=feature&ref_=nv_wl_img_2'
    ]
    page_no = 0

    def parse(self, response):

        items = MovieScraperItem()
        max_pages = int(getattr(self, 'max_pages'))

        movies = response.css(".mode-advanced")

        for movie in movies:
            movie_name = movie.css(
                '.lister-item-header a').css('::text').extract()
            movie_rating = movie.css(
                '.ratings-imdb-rating strong').css('::text').extract()
            movie_cast = movie.css(
                '.lister-item-content .ghost~ a').css('::text').extract()
            yield ({
                "movie_name": movie_name,
                "movie_rating": movie_rating,
                "movie_cast": movie_cast,
            })

        if self.page_no + 1 < max_pages:
            self.page_no = self.page_no + 1
            url = f"https://www.imdb.com/search/title?title_type=feature&count=100&start={(self.page_no * 100)+1}&ref_=adv_nxt"
            yield response.follow(url, callback=self.parse)
