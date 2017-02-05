from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from article.models import Article
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

def index(request):
    article_list = Article.objects.all().order_by('-pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'pages/index.html', context)


def search(request):
    if request.method == 'POST':
        vector = SearchVector('title')
        query = SearchQuery(request.POST.get('search'))
        article_list = Article.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        context = {
                'article_list': article_list
        }
        return render(request, 'pages/index.html', context)
