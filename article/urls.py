from django.conf.urls import include, url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^(?P<category>[\w-]+)/$', views.category_list, name='categoryList'),
    url(r'^(?P<category>[\w-]+)/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.detail, name='detail'),

]
