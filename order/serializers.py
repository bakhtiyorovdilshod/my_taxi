from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from customer.models import Customer
from .models import AcceptOrder


class CustomerOrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class AcceptOrderCreateSerializer(ModelSerializer):
    class Meta:
        model = AcceptOrder
        fields = "__all__"

    def validate(self, data):
        customer_id = data['customer_phone']
        customer_qs = AcceptOrder.objects.filter(customer_phone=customer_id)
        if customer_qs.exists():
            raise ValidationError("This order has already taken")
        return data

