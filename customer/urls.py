from django.urls import path
from .views import FilterOrdersAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('see/order/status/', FilterOrdersAPIView.as_view(), name='see order status')

]
urlpatterns = format_suffix_patterns(urlpatterns)


