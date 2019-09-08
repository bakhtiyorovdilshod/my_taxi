from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class CustomerOrdersLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 4
    default_limit = 2