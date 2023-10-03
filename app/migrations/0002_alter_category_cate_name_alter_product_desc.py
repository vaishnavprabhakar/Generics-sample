# Generated by Django 4.2.5 on 2023-09-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cate_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(verbose_name='Product description'),
        ),
    ]
