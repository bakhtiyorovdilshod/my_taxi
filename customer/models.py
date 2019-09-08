from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number is error")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.phone_number





