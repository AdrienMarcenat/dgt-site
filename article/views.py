from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article

class ArticleDetail(DetailView):
    model = Article

class ArticleList(ListView):
    model = Article

def detail(request, article_title):
    return HttpResponse("You're reading article %s." % article_title)

def list(request):
    return HttpResponse("You're looking at the article list")
