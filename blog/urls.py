from django.urls import include, path

from blog.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/detail/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
