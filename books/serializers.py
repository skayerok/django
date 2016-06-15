from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'author', 'book_year', 'isbn', 'page_count', 'voting_closed', 'voters', 'image')
