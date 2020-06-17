from django.db import models


class Measure(models.Model):
    """
    Единица измерения
    """
    title = models.CharField(max_length=50, unique=True)
    short_title = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title


class Characteristic(models.Model):
    """
    Характеристика товара
    """
    title = models.CharField(max_length=100, unique=True)
    short_title = models.CharField(max_length=50, unique=True)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
