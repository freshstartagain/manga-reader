from mangareaderapi import ma


class MangaSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "published", "status", "image")


class AuthorSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "created_on", "updated_on")


class ArtistSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "created_on", "updated_on")


class GenreSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "created_on", "updated_on")


manga_schema = MangaSchema()
mangas_schema = MangaSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
