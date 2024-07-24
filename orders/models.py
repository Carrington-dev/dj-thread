from django.db import models
from .utils import order_number_generator, length

class Order(models.Model):
    first_name = models.CharField(max_length=length, blank=True, null=True)
    last_name = models.CharField(max_length=length, blank=True, null=True)
    email = models.EmailField(max_length=length)
    order_number = models.CharField(max_length=length, default=order_number_generator)


    def __str__(self):
        return f"{self.email} {self.order_number}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'