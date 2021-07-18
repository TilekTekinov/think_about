from rest_framework.serializers import ModelSerializer, CharField

from blog.models import Category, Article


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        """ Representation Category parent """
        self.fields['parent'] = CategoryListSerializer(read_only=True)
        return super(CategoryListSerializer, self).to_representation(instance)


class ArticleListSerializer(ModelSerializer):
    category = CategoryListSerializer()
    user = CharField()

    class Meta:
        model = Article
        fields = '__all__'
