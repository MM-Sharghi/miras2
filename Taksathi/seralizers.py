from Users.models import Users
from rest_framework import serializers
from .models import *
from django.db.models.fields import TextField

class ProductsSerializers(serializers.ModelSerializer):
    price = serializers.IntegerField(required=True)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Products
        fields = '__all__'


class ProductMainCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductMainCategories
        fields = '__all__'

class ProductSubCategories_1Serializers(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategories_1
        fields = '__all__'

class ProductSubCategories_2Serializers(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategories_2
        fields = '__all__'




class ProductsUpdateSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    descriptions = TextField(null=True,blank=True)
    image = serializers.ImageField(required=False)
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    image3 = serializers.ImageField(required=False)
    price = serializers.IntegerField(required=False)
    maincategories = serializers.PrimaryKeyRelatedField(queryset=ProductMainCategories.objects.all(), many=True)
    subCategories1 = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategories_1.objects.all(), many=True)
    subCategories2 = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategories_2.objects.all(), many=True)
    volume = serializers.CharField(required=False)
    compounds = serializers.CharField(required=False)
    licenseـissuer = serializers.CharField(required=False)
    limit = serializers.IntegerField(required=False)
    jdate = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.user)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.descriptions = validated_data.get('descriptions', instance.descriptions)
        instance.image = validated_data.get('image', instance.image)
        instance.image1 = validated_data.get('image1', instance.image1)
        instance.image2 = validated_data.get('image2', instance.image2)
        instance.image3 = validated_data.get('image3', instance.image3)
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
    product_image = serializers.ReadOnlyField()
    user_address = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = ProductsOrders
        fields = '__all__'


class ProductsCommentsSerializers(serializers.ModelSerializer):
    user_fullname = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = ProductsComments
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    mobile1 = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Users
        fields = ['mobile1','jdate','password']

    def update(self, instance, validated_data):
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        if instance.password == validated_data.get('password'):
            pass
        else:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class TiketSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
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
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Tiket
        fields = '__all__'



    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class MessagesSupportSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    class Meta:
        model = Messages
        fields = ['user','tiket','jdate','status','text','file']


class MessagesUserSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    class Meta:
        model = Messages
        fields = ['user','tiket','support','jdate','status','text','file']
        extra_kwargs = {
            "support": {"error_messages": {"required": "This amount is required"}},
        }




