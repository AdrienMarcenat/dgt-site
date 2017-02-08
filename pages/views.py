from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from article.models import Article

def index(request):
    article_list = Article.objects.all().order_by('-pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'pages/index.html', context)


def search(request):
    if request.method == 'POST':
        search_input = request.POST.get('search')
        article_list = Article.objects.all().filter(title__contains=search_input)
        context = {
                'article_list': article_list,
                'search_input': search_input
        }
        return render(request, 'pages/index.html', context)
