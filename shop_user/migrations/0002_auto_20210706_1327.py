# Generated by Django 3.2.5 on 2021-07-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]