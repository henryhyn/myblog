from django.shortcuts import render
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def show(request, id):
    article = models.Article.objects.get(pk=id)
    return render(request, 'blog/show.html', {'article': article})
