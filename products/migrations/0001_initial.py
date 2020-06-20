# Generated by Django 3.0.7 on 2020-06-20 19:40

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, help_text='Discount price', max_digits=5, verbose_name='Sale price')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='shop_categories')),
                ('description', models.TextField(blank=True, verbose_name='Category description')),
                ('show_in_top', models.BooleanField(default=True, verbose_name='Show in top')),
                ('show_in_sidebar', models.BooleanField(default=True, verbose_name='Show in sidebar')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='products')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='products', to='products.ProductImage'),
        ),
    ]
