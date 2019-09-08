from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    CustomerOrderCreateAPIView,
    AcceptOrderCreateAPIView,
)


urlpatterns = [
    path('customer/create/', CustomerOrderCreateAPIView.as_view(), name='order create'),
    path('accept/', AcceptOrderCreateAPIView.as_view(), name='accept'),

]
urlpatterns = format_suffix_patterns(urlpatterns)


