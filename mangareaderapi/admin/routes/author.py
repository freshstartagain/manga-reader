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
    return jsonify(result)


@author.route("/author<id>", methods=["GET"])
def get_author(id):
    author = Author.query.get(id)
    result = author_schema.jsonify(author)

    return result


@author.route("/author", methods=["POST"])
def add_author():
    name = request.json["name"]

    if check_existing_by_name(name, Author):
        return jsonify(message=f"The author is already existing")
    else:
        new_author = Author(name)

        db.session.add(new_author)
        db.session.commit()

        return author_schema.jsonify(new_author)


@author.route("/author/<id>", methods=["PUT"])
def update_author(id):
    author = Author.query.get(id)

    if author:
        name = request.json["name"]

        author.name = name

        db.session.commit()

        return author_schema.jsonify(author)
    else:
        return jsonify(message=f"The author does not exist")


@author.route("/author/<id>", methods=["DELETE"])
def delete_author(id):
    author = Author.query.get(id)

    if author:
        db.session.delete(author)
        db.session.commit()

        return author_schema.jsonify(author)
    else:
        return jsonify(message="The author does not exist")
