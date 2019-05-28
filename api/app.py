from flask import Flask, request, redirect
from flask_pymongo import MongoClient
from bson.objectid import ObjectId
import csv
import json

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1', 27017)


def upload_file(file):
    db = client['movie-db']
    movies = db.movies
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        count = 0
        for row in reader:
            movie_id = movies.insert_one(row).inserted_id
            count += 1
        print(f'Uploaded {count} movies.')
    return 'Movies Uploaded'


dbs = client.list_database_names()
if 'movie-db' in dbs:
    print("Database already exits")
    db = client['movie-db']
else:
    upload_file('../movie_scraper/movies1000.csv')



