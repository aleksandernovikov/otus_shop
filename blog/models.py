from django.contrib.auth import get_user_model
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from categories.models import PostCategory

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

    image = ThumbnailerImageField(upload_to='posts', blank=True)

    title = models.CharField(max_length=150)
    slug = models.SlugField()

    text = models.TextField()
