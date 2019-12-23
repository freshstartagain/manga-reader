from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from mangareaderapi.config import Config


# Init app
app = Flask(__name__)
app.config.from_object(Config)


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

