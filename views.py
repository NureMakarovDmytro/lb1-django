from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


def articles_by_author(request, author_name):
    articles = Article.objects.filter(author=author_name).order_by('-published_at')
    return render(request, 'articles/articles_by_author.html', {
        'articles': articles,
        'author': author_name,
    })
