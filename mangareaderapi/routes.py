from flask import request, jsonify
from mangareaderapi import app, db
from mangareaderapi.models import Manga, Author, Artist, Genre
from mangareaderapi.schema import (
    manga_schema,
    mangas_schema,
    genre_schema,
    genres_schema,
)

# Manga Routes
@app.route("/manga", methods=["GET"])
def get_mangas():
    all_mangas = Manga.query.all()
    result = mangas_schema.dump(all_mangas)
    return jsonify(result)


# Genre Routes
@app.route("/genre", methods=["GET"])
def get_genres():
    all_genres = Genre.query.all()
    result = genres_schema.dump(all_genres)
    return jsonify(result)


@app.route("/genre/<id>", methods=["GET"])
def get_genre(id):
    genre = Genre.query.get(id)
    return genre_schema.jsonify(genre)


@app.route("/genre", methods=["POST"])
def add_genre():
    name = request.json["name"]

    new_genre = Genre(name)

    db.session.add(new_genre)
    db.session.commit()

    return genre_schema.jsonify(new_genre)

@app.route("/genre/<id>", methods=["PUT"])
def update_genre(id):
    genre = Genre.query.get(id)

    name = request.json["name"]

    genre.name = name

    db.session.commit()

    return genre_schema.jsonify(genre)
    
@app.route("/genre/<id>", methods=["DELETE"])
def delete_genre(id):
    genre = Genre.query.get(id)

    db.session.delete(genre)
    db.session.commit()

    return genre_schema.jsonify(genre)

