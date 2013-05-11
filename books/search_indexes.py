from haystack.indexes import *
from haystack import site
from books.models import Book


class BookIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author')
    #pub_date = indexes.DateTimeField(model_attr='pub_date')

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Book.objects.all()

site.register(Book, BookIndex)