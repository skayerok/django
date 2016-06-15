from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book
from .forms import AddBook


def index(request):
    """method is_voted to Book model.
    Checks, if user already voted for the Book"""

    if not request.user.is_authenticated():
        return redirect(LOGIN_URL)
    data = {'books': Book.objects.all()}
    return render(request, 'books/index.html', data)


LOGIN_URL = '/login'
CATALOG_URL = '/books'


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def new_book(request):
    if not request.user.is_authenticated():
        return redirect(LOGIN_URL)
    if request.method == 'POST':
        form = AddBook(request.POST, request.FILES)
        if form.is_valid():
            book = Book(
                book_name=form.cleaned_data['book_name'],
                author=form.cleaned_data['author'],
                book_year=form.cleaned_data['book_year'],
                isbn=form.cleaned_data['isbn'],
                page_count=form.cleaned_data['page_count'],
                voting_closed=False,
                image=request.FILES['image']
            )
            book.save()
            return HttpResponseRedirect(CATALOG_URL)
    else:
        form = AddBook()
    return render(request, 'books/new_book.html', {'form': form})


def detail(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'books/book_detail.html', {'book': book})


def vote(request, book_id):
    if not request.user.is_authenticated():
        return redirect(LOGIN_URL)
    book = Book.objects.get(id=book_id)
    if request.user in book.voters.all():
        book.voters.remove(request.user)
    else:
        book.voters.add(request.user)
    book.save()
    return HttpResponseRedirect(CATALOG_URL)

