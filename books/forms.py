from django import forms
import datetime


class AddBook(forms.Form):
    book_name = forms.CharField(label='Book name', max_length=300)
    author = forms.CharField(label='Author', max_length=200)
    book_year = forms.IntegerField(label='Publish year', min_value=1900, max_value=datetime.datetime.today().year)
    isbn = forms.CharField(label='ISBN', max_length=20)
    page_count = forms.IntegerField(label='Page count', min_value=0)
    image = forms.ImageField(label='Book cover', max_length=100)


class Authorization(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=40)
