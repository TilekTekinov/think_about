from django.urls import include, path

from api.views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list-api'),
    path('articles/', ArticleListView.as_view(), name='article-list-api')
]