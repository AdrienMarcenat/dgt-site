from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

def detail(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    context = {
        'article': article,
    }
    return render(request, 'articles/article.html', context)

def gameDesign(request):
    article_list = Article.objects.filter(tags__tag='Game Design').order_by('pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/game_design_list.html', context)

def musique(request):
    article_list = Article.objects.filter(tags__tag='Musique').order_by('pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/musique_list.html', context)

def developpement(request):
    article_list = Article.objects.filter(tags__tag='Developpement').order_by('pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/developpement_list.html', context)
