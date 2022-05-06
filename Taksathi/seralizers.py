from Users.models import Users
from rest_framework import serializers
from .models import *

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsOrders
        fields = '__all__'


class ProductsCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsComments
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['mobile1','password']

    def update(self, instance, validated_data):
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        if instance.password == validated_data.get('password'):
            pass
        else:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance



