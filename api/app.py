from flask import Flask, request, abort
from flask_pymongo import MongoClient
from bson.objectid import ObjectId
import csv
import json

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1', 27017)


def upload_file(file):
    db = client['movie-db']
    movies = db.movies
    try:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            count = 0
            for row in reader:
                movie_id = movies.insert_one(row).inserted_id
                count += 1
            print(f'Uploaded {count} movies.')
    except Exception:
        return False

    return True


dbs = client.list_database_names()
if 'movie-db' in dbs:
    print("Database already exits")
    db = client['movie-db']
else:
    upload_file('../movie_scraper/movies1000.csv')


@app.route('/autocomplete')
def autocorrect():
    prefix = request.args.get("prefix")
    if prefix is None:
        return abort(400)
    limit = request.args.get("limit")
    if limit is None:
        limit = 5
    offset = request.args.get("offset")
    if offset is None:
        offset = 0

    db = client['movie-db']
    movies = db.movies
    names = []
    movie_names = movies.find(
        {"movie_name": {"$regex": "^" + prefix, "$options": "$i"}})
    for name in movie_names:
        names.append(name["movie_name"])
    movie_like = {
        "movie_names": names
    }

    return json.dumps(movie_like, indent=2)


@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    db = client['movie-db']
    movies = db.movies
    movie = movies.find_one({"_id": ObjectId(movie_id)})
    movie_detail = {
        "movie_name": movie["movie_name"],
        "rating": movie["movie_rating"],
        "cast": movie["movie_cast"]
    }
    return json.dumps(movie_detail, indent=2)
