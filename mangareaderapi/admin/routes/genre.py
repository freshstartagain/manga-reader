from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Genre
from mangareaderapi.schema import genre_schema, genres_schema

genre = Blueprint('genre', __name__)

# Genre Routes
@genre.route("/genre", methods=["GET"])
def get_genres():
    all_genres = Genre.query.all()
    result = genres_schema.dump(all_genres)
    return jsonify(result)


@genre.route("/genre/<id>", methods=["GET"])
def get_genre(id):
    genre = Genre.query.get(id)
    return genre_schema.jsonify(genre)


@genre.route("/genre", methods=["POST"])
def add_genre():
    name = request.json["name"]

    new_genre = Genre(name)

    db.session.add(new_genre)
    db.session.commit()

    return genre_schema.jsonify(new_genre)


@genre.route("/genre/<id>", methods=["PUT"])
def update_genre(id):
    genre = Genre.query.get(id)

    name = request.json["name"]

    genre.name = name

    db.session.commit()

    return genre_schema.jsonify(genre)


@genre.route("/genre/<id>", methods=["DELETE"])
def delete_genre(id):
    genre = Genre.query.get(id)

    db.session.delete(genre)
    db.session.commit()

    return genre_schema.jsonify(genre)

