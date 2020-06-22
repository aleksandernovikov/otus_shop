from django.core import management
from django.core.management import BaseCommand


class Command(BaseCommand):
    # @staticmethod
    # def add_measures():
    #     data = [
    #         {'title': 'Граммы', 'short_title': 'гр.'},
    #         {'title': 'Сантиметры', 'short_title': 'см.'},
    #     ]
    #     measure_objects = [Measure(**params) for params in data]
    #     Measure.objects.bulk_create(measure_objects, ignore_conflicts=True)

    # @staticmethod
    # def add_characteristics():
    #     data = [
    #         {'title': 'Вес в граммах', 'short_title': 'Вес', 'measure': Measure.objects.get(title='Граммы')},
    #         {'title': 'Диаметр в сантиметрах', 'short_title': 'Диаметр',
    #          'measure': Measure.objects.get(title='Сантиметры')},
    #     ]
    #     characteristics_objects = [Characteristic(**params) for params in data]
    #     Characteristic.objects.bulk_create(characteristics_objects, ignore_conflicts=True)

    # @staticmethod
    # def add_products():
    #     data = [
    #         {'category': ProductCategory.objects.get(title='На тонком тесте'), 'title': 'Пепперони'}
    #     ]
    #     product_objects = [Product(**params) for params in data]
    #     Product.objects.bulk_create(product_objects, ignore_conflicts=True)
    #
    # @staticmethod
    # def add_product_variants():
    #     data = [
    #         {'parent_product': Product.objects.get(title='Пепперони'), 'title': 'Большая'},
    #         {'parent_product': Product.objects.get(title='Пепперони'), 'title': 'Нормальная'},
    #     ]
    #     variant_object = [ProductVariant(**params) for params in data]
    #     print(variant_object)
    #     ProductVariant.objects.bulk_create(variant_object, ignore_conflicts=True)

    def handle(self, *args, **options):
        management.call_command('loaddata', 'user')
        management.call_command('loaddata', 'blog')
        management.call_command('loaddata', 'product_categories')
        management.call_command('loaddata', 'products')
        management.call_command('loaddata', 'product_images')
