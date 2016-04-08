# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.core.paginator import InvalidPage, Paginator

from .models import Column, Article

def index(request):
    articles = Article.objects.filter(published=True,deleted=False).order_by('-pub_date')

    paginator = Paginator(articles, 3)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'index.html',{'page':page})

def message(request):
    return render(request, 'message.html')

def about(request):
    return render(request, 'about.html')

def columns(request):
	columns=Column.objects.all().order_by('important_num')
	return render(request,'columns_list.html',{"columns":columns})

def column_detail(request, column_slug):

    column = get_object_or_404(Column,slug=column_slug)
    articles = Article.objects.filter(column=column,published=True,deleted=False).order_by('-pub_date')

    paginator = Paginator(articles, 3)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'index.html',{'page':page})
    return render(request, 'column_detail.html', {'page': page,'column':column})


def article(request, pk):

    article = get_object_or_404(Article, pk=pk, published=True, deleted=False)

    return render(request, 'article.html', {'article': article})