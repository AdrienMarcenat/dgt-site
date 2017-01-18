from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

def detail(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    article_list = Article.objects.all()
    context = {
        'article': article,
        'article_list': article_list
    }
    return render(request, 'articles/article.html', context)

def archives(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/article_list.html', context)

def gameDesign(request):
    article_list = Tag.objects.filter(tag="Game Design").select_related('article__tags')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/article.html', context)

def musique(request):
    article_list = Tag.objects.filter(tag="Musique").select_related('article__tags')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/article.html', context)

def developpement(request):
    article_list = Tag.objects.filter(tag="Developpement").select_related('article__tags')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/article.html', context)
