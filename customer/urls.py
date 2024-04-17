from django.urls import path
from .views import *

app_name = 'customer'
urlpatterns = [
    path('customer_detail/<int:pk>/', customer_detail, name='customer_detail'),
    path('cart/', customer_cart, name='customer_cart'),
    path("modify_cart/", modify_cart, name='modify_cart'),
    
]