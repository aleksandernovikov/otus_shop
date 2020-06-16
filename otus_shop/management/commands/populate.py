from django.core.management import BaseCommand

from otus_shop.models import Measure, Characteristic, ProductCategory


class Command(BaseCommand):
    @staticmethod
    def add_measures():
        data = [
            {'title': 'Граммы', 'short_title': 'гр.'},
            {'title': 'Сантиметры', 'short_title': 'см.'},
        ]
        measure_objects = [Measure(**params) for params in data]
        Measure.objects.bulk_create(measure_objects, ignore_conflicts=True)

    @staticmethod
    def add_characteristics():
        data = [
            {'title': 'Вес в граммах', 'short_title': 'Вес', 'measure': Measure.objects.get(title='Граммы')},
            {'title': 'Диаметр в сантиметрах', 'short_title': 'Диаметр',
             'measure': Measure.objects.get(title='Сантиметры')},
        ]
        characteristics_objects = [Characteristic(**params) for params in data]
        Characteristic.objects.bulk_create(characteristics_objects, ignore_conflicts=True)

    @staticmethod
    def add_categories():
        data = [
            {'title': 'Пицца', 'depth': 1},
        ]
        categories_objects = [ProductCategory(**params) for params in data]
        ProductCategory.objects.bulk_create(categories_objects, ignore_conflicts=True)

    def handle(self, *args, **options):
        self.add_measures()
        self.add_characteristics()
        self.add_categories()
