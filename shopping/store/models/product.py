from django.db import models
from unicodedata import category

from .category import  Category


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Description = models.CharField(max_length=200, default='', blank=True, null=True)
    Image = models.ImageField(upload_to='Upload/products/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()



    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(Category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.Name