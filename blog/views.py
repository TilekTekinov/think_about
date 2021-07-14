from django.shortcuts import render
from blog.models import *
from blog.filters import *
from django.views.generic import TemplateView, ListView, DetailView
from django_filters.views import FilterView


class IndexView(FilterView):
    model = Article
    filterset_class = ArticleFilter
    template_name = 'pages/index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'pages/article_detail.html'
