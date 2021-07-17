from account.views import *
from django.urls import path

urlpatterns = [
    path('create/', SignUpView.as_view(), name='user-create'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
    path('password_change/', UpdatePassword.as_view(), name='password-change')
]
