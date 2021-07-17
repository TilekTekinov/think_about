from rest_framework.generics import ListAPIView

from blog.models import Category, Article
from api.serializers import CategoryListSerializer, ArticleListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer