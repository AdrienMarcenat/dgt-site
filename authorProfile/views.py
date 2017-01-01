from django.shortcuts import render
from .models import AuthorProfile
from article.models import Article

def list(request):
    authorProfile_list = AuthorProfile.objects.all()
    article_list = Article.objects.all()
    context = {
        'authorProfile_list': authorProfile_list,
        'article_list': article_list
    }
    return render(request, 'authorProfile/authorProfile.html', context)
