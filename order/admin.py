from django.contrib import admin
from .models import OrderStatus, AcceptOrder

admin.site.register(OrderStatus)
admin.site.register(AcceptOrder)
