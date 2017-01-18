from django.conf.urls import include, url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^article/(?P<article_title>[a-z, A-Z]+)/$', views.detail, name='detail'),
    url(r'^gameDesign/$', views.gameDesign, name='GameDesign'),
    url(r'^developpement/$', views.developpement, name='Developpement'),
    url(r'^musique/$', views.musique, name='Musique'),
    url(r'^archives/$', views.archives, name='Archives'),
]


