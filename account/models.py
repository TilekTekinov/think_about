from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
