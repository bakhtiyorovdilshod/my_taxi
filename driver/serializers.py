from rest_framework.serializers import ModelSerializer
from customer.models import Customer
from order.models import AcceptOrder
from customer.serializers import GetOrderStatusSerializer


class CustomerOrderListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"



class UpdateOrderStatusSerializer(ModelSerializer):
    order_status = GetOrderStatusSerializer(read_only=True, many=False)

    class Meta:
        model = AcceptOrder
        fields = [
            "order_status"
        ]


class GetCustomerPhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "phone_number"
        ]


class FilterAcceptedOrderForDriverSerializer(ModelSerializer):
    order_status = GetOrderStatusSerializer(read_only=True, many=False)
    customer_phone = GetCustomerPhoneNumberSerializer(read_only=True, many=False)

    class Meta:
        model = AcceptOrder
        fields = [
            "order_status",
            "customer_phone",
            "created",
            "updated"
        ]


