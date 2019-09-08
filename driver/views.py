from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import (
    CustomerOrderListSerializer,
    UpdateOrderStatusSerializer,
    FilterAcceptedOrderForDriverSerializer
)
from customer.models import Customer
from order.models import AcceptOrder
from .pagination import CustomerOrdersLimitOffsetPagination


class CustomerOrderListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerOrderListSerializer
    pagination_class = CustomerOrdersLimitOffsetPagination


class UpdateOrderStatusAPIView(RetrieveUpdateAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = UpdateOrderStatusSerializer


class FilterAcceptedOrderForDriverAPIView(ListAPIView):
    serializer_class = FilterAcceptedOrderForDriverSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = AcceptOrder.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(car_number__icontains=query)
            ).distinct()
        return queryset_list









