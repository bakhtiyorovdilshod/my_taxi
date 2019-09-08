from django.core.validators import RegexValidator
from django.db import models
from customer.models import Customer


class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class AcceptOrder(models.Model):
    customer_phone = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Your phone number is error!")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    car_number_regex = RegexValidator(regex=r'^\d{2}\w{1}\d{3}\w{2}$', message="Your car number is error!")
    car_number = models.CharField(max_length=20, blank=False, validators=[car_number_regex])
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name



