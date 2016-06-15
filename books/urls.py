from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = 'books'

router = routers.DefaultRouter()
router.register(r'api', views.BookViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'new_book/$', views.new_book, name='new_book'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='book-detail'),
    url(r'^(?P<book_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
