from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(get_random_secret_key())
