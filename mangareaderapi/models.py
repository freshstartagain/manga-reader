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
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
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
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestam(), nullable=False
    )
    mangas = db.relationship("Manga", backref="author", lazy=True)

    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestam(), nullable=False
    )
    mangas = db.relationship("Manga", backref="artist", lazy=True)

    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    def __init__(self, name):
        self.name = name
