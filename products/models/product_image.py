from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='product_images', on_delete=models.CASCADE)
    image = ThumbnailerImageField(upload_to='products')
    order = models.PositiveSmallIntegerField(default=0, db_index=True)

    def __str__(self):
        return self.image.url

    class Meta:
        ordering = ('-order',)
