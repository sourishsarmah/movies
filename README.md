# movies
Show movie details of a movie


# Scraper

Scraps movie details from IMDB site.

Movie Details - 

1. Name
2. Rating
3. Cast


## To Run Scaper

1. Goto movie_scraper directory

2. Run - 

        $scrapy crawl imdb_scraper -a max_pages=[no_of_pages] -o outputfilename.csv
    
    Eg -
    ```bash
    $ scrapy crawl imdb_scraper -a max_pages=10 -o movies1000.csv
    ```