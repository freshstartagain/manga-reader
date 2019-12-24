from flask import request, jsonify, Blueprint
from mangareaderapi import app, db
from mangareaderapi.models import Author
from mangareaderapi.schema import author_schema, authors_schema
from mangareaderapi.admin.routes.utils import check_existing_by_name

author = Blueprint("author", __name__)


@author.route("/author", methods=["GET"])
def get_authors():
    all_authors = Author.query.all()
    result = authors_schema.dump(all_authors)
    return jsonify(result), 200


@author.route("/author/<id>", methods=["GET"])
def get_author(id):
    author = Author.query.get(id)

    if author:
        return author_schema.jsonify(author), 200
    else:
        return jsonify(message="The author does not exist"), 404


@author.route("/author", methods=["POST"])
def add_author():
    name = request.json["name"]

    if check_existing_by_name(name, Author):
        return jsonify(message="The author is already existing"), 400
    else:
        new_author = Author(name)

        db.session.add(new_author)
        db.session.commit()

        return author_schema.jsonify(new_author), 201


@author.route("/author/<id>", methods=["PUT"])
def update_author(id):
    author = Author.query.get(id)

    if author:
        name = request.json["name"]

        author.name = name

        db.session.commit()

        return author_schema.jsonify(author), 200
    else:
        return jsonify(message="The author does not exist"), 400


@author.route("/author/<id>", methods=["DELETE"])
def delete_author(id):
    author = Author.query.get(id)

    if author:
        db.session.delete(author)
        db.session.commit()

        return author_schema.jsonify(author), 200
    else:
        return jsonify(message="The author does not exist"), 400
