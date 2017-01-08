from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from article.models import Article

def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list
    }
    return render(request, 'pages/index.html', context)
