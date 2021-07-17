from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from account.forms import SignUpForm
from account.models import User


class SignUpView(LoginRequiredMixin, CreateView):
    form_class = SignUpForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('article-list')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class UserListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 10
    ordering = ['-id']
    template_name = 'user/user_list.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username',)
    template_name = 'article/create_or_update.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update User'
        return context


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'category/category_delete.html'
    success_url = reverse_lazy('user-list')


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('article-list')
