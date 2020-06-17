from django.contrib import admin

from reference.models import Measure, Characteristic


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    pass


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    pass
