from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book_id>[0-9]+)/$', views.vote, name='vote'),
    url(r'new_book/$', views.new_book, name='new_book'),
]
