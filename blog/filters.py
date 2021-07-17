from blog.models import Article
from django_filters import FilterSet, CharFilter


class ArticleFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Article
        exclude = ['image']
        fields = ('title', 'category', 'user')

