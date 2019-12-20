from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Author
from mangareaderapi.schema import author_schema, authors_schema

author = Blueprint('author', __name__)

# Author
@author.route("/author", methods=["GET"])
def get_authors():
    all_authors = Author.query.all()
    result = authors_schema.dump(all_authors)
    return jsonify(result)


@author.route("/author<id>", methods=["GET"])
def get_author(id):
    author = Author.query.get(id)
    result = author_schema.jsonify(author)

    return result


@author.route("/author", methods=["POST"])
def add_author():
    firstname = request.json["firstname"]
    middlename = request.json["middlename"]
    lastname = request.json["lastname"]

    new_author = Author(first_name, middle_name, last_name)

    db.session.add(new_author)
    db.session.commit()

    return author_schema.jsonify(new_author)


@author.route("/author/<id>", methods=["PUT"])
def update_author(id):
    author = Author.query.get(id)

    firstname = request.json["firstname"]
    middlename = request.json["middlename"]
    lastname = request.json["lastname"]

    author.first_name = firstname
    author.middle_name = middlename
    author.last_name = lastname

    db.session.commit()

    return author_schema.jsonify(author)


@author.route("/author/<id>", methods=["DELETE"])
def delete_author(id):
    author = Author.query.get(id)

    db.session.delete(author)
    db.session.jsonify(author)

    return author_schema.jsonify(author)
