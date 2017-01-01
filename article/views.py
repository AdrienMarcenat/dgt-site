from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Article

class ArticleDetail(DetailView):
    model = Article

class ArticleList(ListView):
    model = Article

def detail(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    article_list = Article.objects.all()
    context = {
        'article': article,
        'article_list': article_list
    }
    return render(request, 'articles/article.html', context)

def list(request):
    return HttpResponse("You're looking at the article list")
