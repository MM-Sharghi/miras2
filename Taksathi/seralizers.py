from rest_framework import serializers
from .models import ProductsOrders

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsOrders
        fields = '__all__'
