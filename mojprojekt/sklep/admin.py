from django.contrib import admin
from .models import Product, Order, OrderedProduct, Complaint

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Complaint)

admin.site.register(OrderedProduct)
# Register your models here.
