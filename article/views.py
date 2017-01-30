from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

def detail(request, category, id, slug):
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article,
    }
    return render(request, 'articles/article.html', context)

def category_list(request, category):
    article_list = Article.objects.filter(category__name=category).order_by('pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/article_list.html', context)
