from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer
from orders.emailer import EmailThread

from threadweb import settings

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        email_thread = EmailThread(response.data, settings.DEFAULT_FROM_EMAIL)
        email_thread.start()
        email_thread.join()
        return response