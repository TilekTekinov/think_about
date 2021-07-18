from rest_framework.generics import ListAPIView

from blog.models import Category, Article
from api.serializers import CategoryListSerializer, ArticleListSerializer


class CategoryListView(ListAPIView):
    """ List all Categories allow any """
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ArticleListView(ListAPIView):
    """ List all Articles allow any """
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
