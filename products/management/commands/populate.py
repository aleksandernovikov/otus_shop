from django.core import management
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('loaddata', 'user')
        management.call_command('loaddata', 'blog')
        management.call_command('loaddata', 'product_categories')
        management.call_command('loaddata', 'products')
        management.call_command('loaddata', 'product_images')
        management.call_command('loaddata', 'product_characteristics')

