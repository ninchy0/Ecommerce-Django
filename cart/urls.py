from django.urls import path
from .views import *
app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('my_cart', CartView.as_view(), name='my_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('checkout/', checkout, name='checkout'),
]
