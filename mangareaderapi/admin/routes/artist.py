from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Artist
from mangareaderapi.schema import artist_schema, artists_schema

artist = Blueprint("artist", __name__)

# Artist
@artist.route("/artist", methods=["GET"])
def get_artists():
    all_artist = Artist.query.all()
    result = artists_schema.dump(all_artist)
    return jsonify(result)


@artist.route("/artist/<id>", methods=["GET"])
def get_artist(id):
    artist = Artist.query.get(id)
    result = artist_schema.jsonify(artist)

    return result


@artist.route("/artist", methods=["POST"])
def add_artist():
    name = request.json["name"]

    new_artist = Artist(name)

    db.session.add(new_artist)
    db.session.commit()

    return artist_schema.jsonify(new_artist)


@artist.route("/artist/<id>", methods=["PUT"])
def update_artist(id):
    artist = Artist.query.get(id)

    name = request.json["name"]

    artist.name = name

    db.session.commit()

    return artist_schema.jsonify(artist)


@artist.route("/artist/<id>", methods=["DELETE"])
def delete_artist(id):
    artist = Artist.query.get(id)

    db.session.delete(artist)
    db.session.commit()

    return artist_schema.jsonify(artist)
