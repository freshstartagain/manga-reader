from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Artist
from mangareaderapi.schema import artist_schema, artists_schema
from mangareaderapi.admin.routes.utils import check_existing_by_name


artist = Blueprint("artist", __name__)


@artist.route("/artist", methods=["GET"])
def get_artists():
    all_artist = Artist.query.all()
    result = artists_schema.dump(all_artist)
    return jsonify(result), 200


@artist.route("/artist/<id>", methods=["GET"])
def get_artist(id):
    artist = Artist.query.get(id)

    if artist:
        return artist_schema.jsonify(artist), 200
    else:
        return jsonify(message="The artist does not exist"), 404


@artist.route("/artist", methods=["POST"])
def add_artist():
    name = request.json["name"]

    if check_existing_by_name(name, Artist):
        return jsonify(message="The artist is already existing"), 400
    else:
        new_artist = Artist(name)

        db.session.add(new_artist)
        db.session.commit()

        return artist_schema.jsonify(new_artist), 201


@artist.route("/artist/<id>", methods=["PUT"])
def update_artist(id):
    artist = Artist.query.get(id)

    if artist:
        name = request.json["name"]

        artist.name = name

        db.session.commit()

        return artist_schema.jsonify(artist), 200
    else:
        return jsonify(message="The artist does not exist"), 400


@artist.route("/artist/<id>", methods=["DELETE"])
def delete_artist(id):
    artist = Artist.query.get(id)

    if artist:
        db.session.delete(artist)
        db.session.commit()

        return artist_schema.jsonify(artist), 200
    else:
        return jsonify(message="The artist does not exist"), 400
