# Generated by Django 3.0.7 on 2020-06-22 12:19

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='posts')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'Post category',
                'verbose_name_plural': 'Post categories',
            },
        ),
    ]
