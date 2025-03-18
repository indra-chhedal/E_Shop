from django.db import models
from unicodedata import category


class Category(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
