from django.test import TestCase
from django.urls import reverse

from .models import Customer
from rest_framework.test import APIClient
from rest_framework import status


class ModelTestCase(TestCase):

    def setUp(self):
        self.first_name = "Durdona"
        self.last_name = "Durdonova"
        self.phone_number = "+99897777777"
        self.customer = Customer(
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number
        )

    def test_model_can_create_a_customer(self):
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.customer_data = {
            'first_name': "Durdona",
            'last_name': "Durdonova",
            'phone_number': "+99897777777"
        }
        self.response = self.client.post(
            reverse('order create'),
            self.customer_data,
            format="json"
        )

    def test_api_get_order_list(self):
        order_list = Customer.objects.get(id=1)
        response = self.client.get(
            reverse('all orders'),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, order_list)

    def test_api_can_create_a_customer(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

