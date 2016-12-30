from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<article_title>[0-9]+)/$', views.detail, name='detail'),
    url(r'^list/$', views.list, name='list')
]


