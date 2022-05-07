from Users.models import Users
from rest_framework import serializers
from .models import *
from django.db.models.fields import TextField

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'




class ProductsUpdateSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    descriptions = TextField(null=True,blank=True)
    image = serializers.ImageField(required=False)
    price = serializers.IntegerField(required=False)
    maincategories = serializers.PrimaryKeyRelatedField(queryset=ProductMainCategories.objects.all(), many=True)
    subCategories1 = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategories_1.objects.all(), many=True)
    subCategories2 = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategories_2.objects.all(), many=True)
    volume = serializers.CharField(required=False)
    compounds = serializers.CharField(required=False)
    licenseـissuer = serializers.CharField(required=False)
    limit = serializers.IntegerField(required=False)

    class Meta:
        model = Products
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.user)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.descriptions = validated_data.get('descriptions', instance.descriptions)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.maincategories.set(validated_data.get('maincategories', instance.maincategories))
        instance.subCategories1.set(validated_data.get('subCategories1', instance.subCategories1))
        instance.subCategories2.set(validated_data.get('subCategories2', instance.subCategories2))
        instance.volume = validated_data.get('volume', instance.volume)
        instance.compounds = validated_data.get('compounds', instance.compounds)
        instance.licenseـissuer = validated_data.get('licenseـissuer', instance.licenseـissuer)
        instance.limit = validated_data.get('limit', instance.limit)
        instance.save()
        return instance


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
        fields = ['user','tiket','status','text','file']


class MessagesUserSerializers(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    class Meta:
        model = Messages
        fields = ['user','tiket','support','text','file']
        extra_kwargs = {
            "support": {"error_messages": {"required": "This amount is required"}},
        }




