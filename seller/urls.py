from django.urls import path
from .views import *

app_name = 'seller'
urlpatterns = [
    path('', seller_index, name='seller_index'),
    path('add_product/', add_product, name='add_product'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/delete/<int:pk>/', product_delete, name='delete_product'),

]