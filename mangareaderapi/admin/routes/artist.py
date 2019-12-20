from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Artist
from mangareaderapi.schema import artist_schema, artists_schema

artist = Blueprint('artist', __name__)

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
    firstname = request.json["firstname"]
    middlename = request.json["middlename"]
    lastname = request.json["lastname"]

    new_artist = Artist(first_name, middle_name, last_name)

    db.session.add(new_artist)
    db.session.commit()

    return author_schema.jsonify(new_author)


@artist.route("/artist/<id>", methods=["PUT"])
def update_artist(id):
    artist = Artist.query.get(id)

    firstname = request.json["firstname"]
    middlename = request.json["middlename"]
    lastname = request.json["lastname"]

    author.first_name = firstname
    author.middle_name = middlename
    author.last_name = lastname

    db.session.commit()

    return artist_schema.jsonify(artist)


@artist.route("/artist/<id>", methods=["DELETE"])
def delete_artist():
    artist = Artist.query.get(id)

    db.session.delete(artist)
    db.session.commit()

    return author_schema.jsonify(artist)
