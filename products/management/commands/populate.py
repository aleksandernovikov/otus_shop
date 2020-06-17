from django.core import management
from django.core.management import BaseCommand

from products.models import Product, ProductVariant
from reference.models import Measure, Characteristic
from usability.models import ProductCategory


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
            {'title': 'Пицца', 'children': [
                {'title': 'На тонком тесте'},
                {'title': 'На толстом тесте'},
            ]},
            {'title': 'Роллы'}
        ]
        for params in data:
            # noinspection PyBroadException
            try:
                root = ProductCategory.add_root(title=params.get('title'))
            except:
                continue
            if params.get('children'):
                # noinspection PyBroadException
                try:
                    [root.add_child(**child_data) for child_data in params.get('children')]
                except:
                    continue

    @staticmethod
    def add_products():
        data = [
            {'category': ProductCategory.objects.get(title='На тонком тесте'), 'title': 'Пепперони'}
        ]
        product_objects = [Product(**params) for params in data]
        Product.objects.bulk_create(product_objects, ignore_conflicts=True)

    @staticmethod
    def add_product_variants():
        data = [
            {'parent_product': Product.objects.get(title='Пепперони'), 'title': 'Большая'},
            {'parent_product': Product.objects.get(title='Пепперони'), 'title': 'Нормальная'},
        ]
        variant_object = [ProductVariant(**params) for params in data]
        print(variant_object)
        ProductVariant.objects.bulk_create(variant_object, ignore_conflicts=True)

    def handle(self, *args, **options):
        management.call_command('loaddata', 'user', verbosity=0)

        self.add_measures()
        self.add_characteristics()
        self.add_categories()
        self.add_products()
        self.add_product_variants()
