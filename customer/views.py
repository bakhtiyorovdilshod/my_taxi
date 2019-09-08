from rest_framework.generics import ListAPIView
from order.models import AcceptOrder
from django.db.models import Q
from .serializers import CustomerOrdersSerializer


class FilterOrdersAPIView(ListAPIView):
    serializer_class = CustomerOrdersSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = AcceptOrder.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(customer_phone__phone_number__icontains=query)
            ).distinct()
        return queryset_list


