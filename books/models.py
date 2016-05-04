from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    book_name = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    book_year = models.IntegerField()
    isbn = models.CharField(max_length=20, unique=True, null=True)
    page_count = models.IntegerField()
    voting_closed = models.BooleanField(default=False)
    voters = models.ManyToManyField(User)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.book_name

