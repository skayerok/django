from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book
from .forms import AddBook

LOGIN_URL = '/login'

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'
    login_url = LOGIN_URL

    def get_queryset(self):
        return Book.objects.all()


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
                votes=0,
                image=request.FILES['image']
            )
            book.save()
            return HttpResponseRedirect('../')
    else:
        form = AddBook()
    return render(request, 'books/new_book.html', {'form': form})


def vote(request, book_id):
    book = Book.objects.filter(pk=book_id)
    return HttpResponse('vote on %s' % Book.objects.get(id=book_id))
