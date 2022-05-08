from rest_framework import serializers
from .models import *

class ContractsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Contracts
        fields = '__all__'

class CardsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Cards
        fields = '__all__'


class UsersSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    father_name = serializers.CharField(required=False)
    id_passport = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    national_code = serializers.CharField(required=False)
    mobile1 = serializers.CharField(required=False)
    marital_status = serializers.CharField(required=False)
    education = serializers.CharField(required=False)
    cityـcode = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    mobile2 = serializers.CharField(required=False)
    dateـofـbirth = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    neighbourhood = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    postalـcode = serializers.CharField(required=False)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Users
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.id_passport = validated_data.get('id_passport', instance.id_passport)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.role = validated_data.get('role', instance.role)
        instance.national_code = validated_data.get('national_code', instance.national_code)
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.education = validated_data.get('education', instance.education)
        instance.cityـcode = validated_data.get('cityـcode', instance.cityـcode)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile2 = validated_data.get('mobile2', instance.mobile2)
        instance.dateـofـbirth = validated_data.get('dateـofـbirth', instance.dateـofـbirth)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.neighbourhood = validated_data.get('neighbourhood', instance.neighbourhood)
        instance.address = validated_data.get('address', instance.address)
        instance.postalـcode = validated_data.get('postalـcode', instance.postalـcode)
        if instance.password == validated_data.get('password'):
            pass
        else:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance





class MainUserSerializers(serializers.ModelSerializer):
    places = serializers.IntegerField(required=True)
    user = serializers.CharField(required=False)
    identifierـcode = serializers.CharField(required=False)
    r_or_l = serializers.BooleanField(required=False)
    class Meta:
        model = MainUser
        fields = '__all__'





class SelectPointsSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    father_name = serializers.CharField(required=False)
    id_passport = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    national_code = serializers.CharField(required=False)
    mobile1 = serializers.CharField(required=False)
    marital_status = serializers.CharField(required=False)
    education = serializers.CharField(required=False)
    cityـcode = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    mobile2 = serializers.CharField(required=False)
    dateـofـbirth = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    neighbourhood = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    postalـcode = serializers.CharField(required=False)
    Book_or_buy_goods = serializers.BooleanField(required=True)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Users
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.id_passport = validated_data.get('id_passport', instance.id_passport)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.role = validated_data.get('role', instance.role)
        instance.national_code = validated_data.get('national_code', instance.national_code)
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.education = validated_data.get('education', instance.education)
        instance.cityـcode = validated_data.get('cityـcode', instance.cityـcode)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile2 = validated_data.get('mobile2', instance.mobile2)
        instance.dateـofـbirth = validated_data.get('dateـofـbirth', instance.dateـofـbirth)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.neighbourhood = validated_data.get('neighbourhood', instance.neighbourhood)
        instance.address = validated_data.get('address', instance.address)
        instance.postalـcode = validated_data.get('postalـcode', instance.postalـcode)
        instance.Book_or_buy_goods = validated_data.get('Book_or_buy_goods', instance.Book_or_buy_goods)
        if instance.password == validated_data.get('password'):
            pass
        else:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance




