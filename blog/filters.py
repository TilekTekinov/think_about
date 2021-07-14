from blog.models import *
from django_filters import *


class ArticleFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Article
        exclude = ['image']
        fields = ('title', 'category', 'user')

