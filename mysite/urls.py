"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers

from . import settings, views
from rest import views as rest_views

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'groups', rest_views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
