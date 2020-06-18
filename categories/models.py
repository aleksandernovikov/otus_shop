from django.db import models
from treebeard.mp_tree import MP_Node


class ProductCategory(MP_Node):
    """
    Категория товара
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    # show_subcategory_products = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = 'title', 'depth'



