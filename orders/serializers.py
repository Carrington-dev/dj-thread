from rest_framework.serializers import ModelSerializer, CharField

from orders.models import Order

class OrderSerializer(ModelSerializer):
    order_number = CharField(read_only=True)

    class Meta:
        model = Order
        fields = [ 'id', "first_name", "last_name", "email", "order_number", ]