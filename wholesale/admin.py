from django.contrib import admin

from .models import Order, Product, Customer, Document

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Document)
