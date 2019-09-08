from django.test import TestCase
from django.urls import reverse

from .models import OrderStatus, AcceptOrder
from rest_framework.test import APIClient
from rest_framework import status
from customer.models import Customer


class ModelTestCase(TestCase):

    def setUp(self):
        self.phone = Customer.objects.create(
            first_name="Dilshod",
            last_name="Bakhtiyorov",
            phone_number="+998912345678"
        )
        self.create_order_status = OrderStatus.objects.create(
            status="Accepted"
        )
        self.customer_phone = self.phone
        self.first_name = "Behzod"
        self.last_name = "Dadaxonov"
        self.phone_number = "+998997877788"
        self.car_number = "01K878PL"
        self.order_status = self.create_order_status
        self.order = AcceptOrder(
            customer_phone=self.customer_phone,
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number,
            car_number=self.car_number,
            order_status=self.order_status
        )
        self.status = "Accepted"
        self.status_order = OrderStatus(status=self.status)

    def test_model_can_create_a_order(self):
        old_count = AcceptOrder.objects.count()
        self.order.save()
        new_count = AcceptOrder.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_status_order(self):
        old_count = OrderStatus.objects.count()
        self.status_order.save()
        new_count = OrderStatus.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        phone = Customer.objects.create(
            first_name="Dilshod",
            last_name="Bakhtiyorov",
            phone_number="+998912345678"
        )
        create_order_status = OrderStatus.objects.create(
            status="Accepted"
        )
        self.order_data = {
            'customer_phone': phone.id,
            'first_name': "Malika",
            'last_name': 'Yordamova',
            'phone_number': "+998977777778",
            'car_number': '30K878PL',
            'order_status': create_order_status.id
        }
        self.response = self.client.post(
            reverse('accept'),
            self.order_data,
            format="json"
        )

    def test_api_can_update_order(self):
        order = AcceptOrder.objects.get()
        new_order_status = OrderStatus.objects.create(status='Order Completed')
        change_order = {
            "order_status": new_order_status.id
        }
        res = self.client.put(
            reverse('update order status', kwargs={
                'pk': order.id
            }),
            change_order,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_create_a_order(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

