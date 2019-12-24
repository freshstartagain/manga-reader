from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Genre
from mangareaderapi.schema import genre_schema, genres_schema
from mangareaderapi.admin.routes.utils import check_existing_by_name

genre = Blueprint("genre", __name__)


@genre.route("/genre", methods=["GET"])
def get_genres():
    all_genres = Genre.query.all()
    result = genres_schema.dump(all_genres)
    return jsonify(result)


@genre.route("/genre/<id>", methods=["GET"])
def get_genre(id):
    genre = Genre.query.get(id)

    if genre:
        return genre_schema.jsonify(genre)
    else:
        return jsonify(message="The genre does not exist"), 404


@genre.route("/genre", methods=["POST"])
def add_genre():
    name = request.json["name"]

    if check_existing_by_name(name, Genre):
        return jsonify(message="The genre is already existing"), 400
    else:
        new_genre = Genre(name)

        db.session.add(new_genre)
        db.session.commit()

        return genre_schema.jsonify(new_genre), 201


@genre.route("/genre/<id>", methods=["PUT"])
def update_genre(id):
    genre = Genre.query.get(id)

    if genre:
        name = request.json["name"]

        genre.name = name

        db.session.commit()

        return genre_schema.jsonify(genre), 200
    else:
        return jsonify(message="The genre does not exist"), 400


@genre.route("/genre/<id>", methods=["DELETE"])
def delete_genre(id):
    genre = Genre.query.get(id)

    if genre:
        db.session.delete(genre)
        db.session.commit()

        return genre_schema.jsonify(genre), 200
    else:
        return jsonify(message="The genre does not exist"), 400

