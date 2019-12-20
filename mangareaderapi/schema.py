from mangareaderapi import ma


class MangaSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "published", "status", "image")


class AuthorSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstname", "middlename", "lastname")


class ArtistSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstname", "middlename", "lastname")


class GenreSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "creation_date")


manga_schema = MangaSchema()
mangas_schema = MangaSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
