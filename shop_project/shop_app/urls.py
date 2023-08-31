from django.urls import path
from .views import *

urlpatterns = [
    path('entities/', EntityFilteredList.as_view(), name='entity-filtered-list'),
    path('products/filter/', ProductFilteredList.as_view(), name='product-filtered-list'),
    path('products/sort/', ProductSortedList.as_view(), name='product-sorted-list'),

    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/filter/', ProductFilteredList.as_view(), name='product-filtered-list'),

    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    path('managers/', ManagerList.as_view(), name='manager-list'),
    path('managers/<int:pk>/', ManagerDetail.as_view(), name='manager-detail'),

    path('carts/', CartList.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart-detail'),

    path('delivery-crews/', DeliveryCrewList.as_view(), name='delivery-crew-list'),
    path('delivery-crews/<int:pk>/', DeliveryCrewDetail.as_view(), name='delivery-crew-detail'),
]