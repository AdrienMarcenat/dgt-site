from django.conf.urls import include, url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^gameDesign/$', views.gameDesign, name='GameDesign'),
    url(r'^developpement/$', views.developpement, name='Developpement'),
    url(r'^musique/$', views.musique, name='Musique'),

    url(r'^gameDesign/(?P<article_title>[a-z, A-Z]+)/$', views.detail, name='gameDesignArticle'),
    url(r'^developpement/(?P<article_title>[a-z, A-Z]+)/$', views.detail, name='developpementArticle'),
    url(r'^musique/(?P<article_title>[a-z, A-Z]+)/$', views.detail, name='musiqueArticle'),

]
