from django.contrib import admin
from blog.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)
