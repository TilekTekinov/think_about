from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    ListView
)

from blog.filters import ArticleFilter
from account.models import User
from blog.models import Category, Article


class ArticleListView(LoginRequiredMixin, FilterView):
    """ List all Articles with filter by category, user or search by title """
    model = Article
    paginate_by = 2
    ordering = ['-id']
    filterset_class = ArticleFilter
    template_name = 'article/article_list.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """ Create new Article """
    model = Article
    fields = ('category', 'title', 'description', 'image')
    template_name = 'article/create_or_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creat new Article'
        return context

    def form_valid(self, form):
        user = get_object_or_404(User, username=self.request.user)
        form.instance.user = user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """ View Article detail """
    model = Article
    template_name = 'article/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Article category, title, description, image fields. User set by logged in user """
    model = Article
    fields = ('category', 'title', 'description', 'image')
    template_name = 'article/create_or_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Article'
        return context


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete Article """
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article-list')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """ Create new Category """
    model = Category
    fields = '__all__'
    template_name = 'article/create_or_update.html'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Category'
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    """ List all Categories """
    model = Category
    paginate_by = 10
    ordering = ['-id']
    template_name = 'category/category_list.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Category title, parent fields """
    model = Category
    fields = '__all__'
    template_name = 'article/create_or_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Category'
        return context


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete Category """
    model = Category
    template_name = 'category/category_delete.html'
    success_url = reverse_lazy('category-list')
