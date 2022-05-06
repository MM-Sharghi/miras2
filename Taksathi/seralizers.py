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


class TiketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tiket
        fields = '__all__'
        extra_kwargs = {
            "support": {"error_messages": {"required": "This amount is required"}},
        }


class TiketSupportUpdateStatusSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(read_only=True,required=False)
    user = serializers.CharField(required=True)
    support = serializers.CharField(read_only=True,required=False)
    status = serializers.BooleanField(required=True,error_messages={"required": "This amount is required"})
    class Meta:
        model = Tiket
        fields = '__all__'



    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class MessagesSupportSerializers(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    class Meta:
        model = Messages
        fields = ['user','tiket','text','file']


class MessagesUserSerializers(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    class Meta:
        model = Messages
        fields = ['user','tiket','support','text','file']
        extra_kwargs = {
            "support": {"error_messages": {"required": "This amount is required"}},
        }




