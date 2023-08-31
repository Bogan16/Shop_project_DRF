from django.contrib import admin
from .models import Customer, Manager, Product, DeliveryCrew, Cart

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Product)
admin.site.register(DeliveryCrew)
admin.site.register(Cart)