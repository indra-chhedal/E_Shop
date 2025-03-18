from email.policy import default

from django.db import models
from.product import Product

class Cart(models.Model):
    phone = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.phone} -{self.product} -{self.quantity} -{self.image} -{self.price}"