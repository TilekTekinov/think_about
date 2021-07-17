from django.urls import include, path

from blog.views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('arctile/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/detail/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article-delete'),

    path('category/list', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category-delete')
]
