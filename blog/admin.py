from django.contrib import admin
from blog.models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_display_links = ('title',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user')
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
