from django.db import models
from treebeard.mp_tree import MP_Node


class ProductCategory(MP_Node):
    """
    Категория товара
    """
    title = models.CharField(max_length=100)

    # show_subcategory_products = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = 'title', 'depth'


class PostCategory(MP_Node):
    """
    Категория поста
    """

    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
