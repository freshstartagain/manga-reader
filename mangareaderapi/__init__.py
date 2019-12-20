from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "manga_reader.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

from mangareaderapi.admin.routes.manga import manga
from mangareaderapi.admin.routes.author import author
from mangareaderapi.admin.routes.artist import artist
from mangareaderapi.admin.routes.genre import genre

app.register_blueprint(manga)
app.register_blueprint(author)
app.register_blueprint(artist)
app.register_blueprint(genre)