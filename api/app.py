from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/autocomplete')
def autocorrect():
    prefix = request.args.get("prefix")
    limit = request.args.get("limit")
    offset = request.args.get("offset")

    return prefix


@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    return movie_id
