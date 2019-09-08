from django.urls import path
from .views import (
    CustomerOrderListAPIView,
    UpdateOrderStatusAPIView,
    FilterAcceptedOrderForDriverAPIView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('orders/list/', CustomerOrderListAPIView.as_view(), name='all orders'),
    path('update/<int:pk>/order/status/', UpdateOrderStatusAPIView.as_view(), name='update order status'),
    path('filter/accepted/orders/', FilterAcceptedOrderForDriverAPIView.as_view(), name='filter accepted orders for drivers' )

]
urlpatterns = format_suffix_patterns(urlpatterns)
