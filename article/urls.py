from django.conf.urls import include, url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^article/(?P<article_title>[a-z, A-Z]+)/$', views.detail, name='detail'),
    url(r'^list/$', views.list, name='list'),
    url(r'^authors_list/$', views.list, name='authors_list'),
    url(r'^use/$', views.list, name='use')
]


