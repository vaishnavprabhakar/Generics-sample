from django.db import models

# Create your models here.


class Category(models.Model):

    cate_name = models.CharField(verbose_name='Category name',
        null=True,
        blank=True,
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.cate_name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    




class Product(models.Model):

    category_name = models.ForeignKey(
        Category, on_delete=models.CASCADE,
    )

    product_name = models.CharField(max_length=50)
    
    desc = models.TextField(
        'Product description'
    )



    