from rest_framework.generics import (
    CreateAPIView
)
from customer.models import Customer
from .serializers import (
    CustomerOrderCreateSerializer,
    AcceptOrderCreateSerializer
)
from .models import AcceptOrder


class CustomerOrderCreateAPIView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerOrderCreateSerializer


class AcceptOrderCreateAPIView(CreateAPIView):
    queryset = AcceptOrder.objects.all()
    serializer_class = AcceptOrderCreateSerializer

