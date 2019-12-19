from mangareaderapi import ma

class MangaSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "published", "status", "image")


class GenreSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "creation_date")


manga_schema = MangaSchema()
mangas_schema = MangaSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
