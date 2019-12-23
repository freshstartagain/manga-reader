from mangareaderapi import db

genres = db.Table(
    "genres",
    db.Column("genre_id", db.Integer, db.ForeignKey("genre.id"), primary_key=True),
    db.Column("manga_id", db.Integer, db.ForeignKey("manga.id"), primary_key=True),
)


class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    image = db.Column(db.String(20), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    author_id = db.Column(
        db.Integer, db.ForeignKey("author.id", ondelete="CASCADE"), nullable=False
    )
    artist_id = db.Column(
        db.Integer, db.ForeignKey("artist.id", ondelete="CASCADE"), nullable=False
    )
    genres = db.relationship(
        "Genre",
        secondary=genres,
        lazy="subquery",
        backref=db.backref("mangas", lazy=True),
    )

    def __init__(self, name, published, status, image):
        self.name = name
        self.published = published
        self.status = status
        self.image = image


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    mangas = db.relationship("Manga", backref="author", lazy=True)

    def __init__(self, name):
        self.name = name


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    mangas = db.relationship("Manga", backref="artist", lazy=True)

    def __init__(self, name):
        self.name = name


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, name):
        self.name = name
