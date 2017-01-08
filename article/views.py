from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Article

def detail(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    article_list = Article.objects.all()
    context = {
        'article': article,
        'article_list': article_list
    }
    return render(request, 'articles/article.html', context)

def list(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list
    }
    return render(request, 'articles/article_list.html', context)
