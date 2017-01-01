from django.conf.urls import include, url
from . import views

app_name = 'authorProfile'
urlpatterns = [
    url(r'^list/$', views.list, name='list'),
]
