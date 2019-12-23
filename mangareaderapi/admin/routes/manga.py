from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Manga
from mangareaderapi.schema import manga_schema, mangas_schema

manga = Blueprint('posts', __name__)

# Manga Routes
@manga.route("/manga", methods=["GET"])
def get_mangas():
    all_mangas = Manga.query.all()
    result = mangas_schema.dump(all_mangas)
    return jsonify(result)


@manga.route("/manga/<id>", methods=["GET"])
def get_manga(id):
    manga = Manga.query.get(id)
    result = manga_schema.jsonify(manga)

    return result


@manga.route("/manga", methods=["POST"])
def add_manga():
    name = request.json["name"]
    published = request.json["published"]
    status = request.json["status"]
    image = request.json["image"]
    author = request.json["author_id"]
    artist = request.json["artist_id"]
    genre = request.json["genre_id"]

    author = Author.query.get(author)
    artist = Artist.query.get(artist)
    genre = Genre.query.get(genre)

    new_manga = Manga(name, published, status, image)
    new_manga.author.append(author)
    new_manga.artist.append(artist)
    new_manga.genres.append(genre)

    db.session.add(new_manga)
    db.session.commit()

    return manga_schema.jsonify(new_manga)


@manga.route("/manga/<id>", methods=["PUT"])
def update_manga(id):
    manga = Manga.query.get(id)

    name = request.json["name"]
    published = request.json["published"]
    status = request.json["status"]
    image = request.json["image"]

    manga.name = name
    manga.published = published
    manga.status = status
    manga.image = image

    db.session.commit()

    return manga_schema.jsonify(manga)


@manga.route("/manga/<id>", methods=["DELETE"])
def delete_manga(id):
    manga = Manga.query.get(id)

    db.session.delete(manga)
    db.session.commit()

    return manga_schema.jsonify(manga)
