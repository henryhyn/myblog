from django.shortcuts import render
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def show(request, id):
    article = models.Article.objects.get(pk=id)
    return render(request, 'blog/show.html', {'article': article})


def edit(request, id):
    article = models.Article.objects.get(pk=id)
    return render(request, 'blog/form.html', {'article': article})


def save(request):
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    article = models.Article.objects.get(pk=id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/show.html', {'article': article})
