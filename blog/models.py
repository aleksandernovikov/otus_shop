import pytils as pytils
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from treebeard.mp_tree import MP_Node

User = get_user_model()


class PostCategory(MP_Node):
    """
    Категория поста
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = pytils.translit.slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Post category')
        verbose_name_plural = _('Post categories')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(PostCategory, related_name='posts', on_delete=models.CASCADE)

    image = ThumbnailerImageField(upload_to='posts', blank=True)

    title = models.CharField(max_length=150)
    slug = models.SlugField()

    text = models.TextField()

    def __str__(self):
        return f'{self.category.title} : {self.title}'

    @property
    def comments_count(self):
        return 5

    @cached_property
    def short_text(self):
        import re
        from django.utils.html import strip_tags
        text_only = re.sub('[ \t\n]+', ' ', strip_tags(self.text))
        return text_only.strip()
