from django.contrib import admin
from django.urls import path
# from .views import home,signup,
from store import views


urlpatterns = [
    path('',views.home, name='homepage'),#for home page
    path('signup',views.Signup.as_view(), name='signup'),#for signup page
    path('login',views.Login.as_view(), name='login'),#for login page
    path('product-detail/<int:pk>',views.productdetail, name='product-detail'),#for productdtail page
    path('logout',views.logout, name='logout'),#for logout page
    path('add_to_cart',views.add_to_cart, name='add_to_cart'), #for add to cart
    path('show_cart',views.show_cart, name='show_cart'),  #for show cart
    path('plus_cart',views.plus_cart, name='plus_cart'), #for plus cart
    path('minus_cart',views.minus_cart, name='minus_cart'), #for minus cart
    path('remove_cart',views.remove_cart, name='remove_cart') #for remove cart




]
