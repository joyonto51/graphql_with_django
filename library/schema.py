import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from library.models import Writer, Book, Edition


# Type For All Models
class WriterType(DjangoObjectType):
    class Meta:
        model = Writer

class EditionType(DjangoObjectType):
    class Meta:
        model = Edition

class BookType(DjangoObjectType):
    class Meta:
        model = Book


# QueryType

class Query(ObjectType):
    writer = graphene.Field(WriterType, id=graphene.Int())
    edition = graphene.Field(EditionType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())

    writers = graphene.List(WriterType)
    editions = graphene.List(EditionType)
    books = graphene.List(BookType)

    def resolve_writer(self, *args, **kwargs):
        id = kwargs.get('id', None)

        if id:
            return Writer.objects.get(id=id)

        return None

    def resolve_edition(self, *args, **kwargs):
        id = kwargs.get('id', None)

        if id:
            return Edition.objects.get(id=id)

        return None

    def resolve_book(self, **kwargs):
        id = kwargs.get('id', None)

        if id:
            return Book.objects.get(id=id)

        return None

    def resolve_writers(self, **kwargs):
        return Writer.objects.all()

    def resolve_editions(self, **kwargs):
        return Edition.objects.all()

    def resolve_books(self, **kwargs):
        return Book.objects.all()