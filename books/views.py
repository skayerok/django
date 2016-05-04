from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Book
from .forms import AddBook

LOGIN_URL = 'login'


def index(request):
    if not request.user.is_authenticated():
        return redirect(LOGIN_URL)
    data = {'books': Book.objects.all()}
    return render(request, 'books/index.html', data)


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
            return HttpResponseRedirect('../')  # mb should replace with just 'redirect'
    else:
        form = AddBook()
    return render(request, 'books/new_book.html', {'form': form})


def vote(request, book_id):
    book = Book.objects.filter(pk=book_id)
    return HttpResponse('vote on %s' % Book.objects.get(id=book_id))
