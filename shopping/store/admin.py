from django.contrib import admin

# Register your models here.

from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.cart import Cart

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','Price','Name','Category','Description']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','name','phone']

class AdminCart(admin.ModelAdmin):
    list_display = ['id','phone','product','image','price']

admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Cart,AdminCart)


