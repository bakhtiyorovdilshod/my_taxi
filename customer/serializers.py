from rest_framework.serializers import ModelSerializer
from order.models import AcceptOrder, OrderStatus


class GetOrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = [
            "status"
        ]


class CustomerOrdersSerializer(ModelSerializer):
    order_status = GetOrderStatusSerializer(read_only=True, many=False)

    class Meta:
        model = AcceptOrder
        fields = [
            "order_status"
        ]
