from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .seralizers import OrdersSerializers
from .models import ProductsOrders,ProductsCarts,Products
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class carts_add(generics.CreateAPIView):
    serializer_class = OrdersSerializers

    def post(self, request, *args, **kwargs):
        data = OrdersSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            cart = ProductsCarts.objects.filter(user_id=token_info.user.id).first()
            if cart is None:
                cart_create = ProductsCarts.objects.create(user_id=token_info.user.id)
            else: pass
            cart = ProductsCarts.objects.filter(user_id=token_info.user.id).first()
            product = Products.objects.filter(id=data.validated_data['product'].id).first()
            ProductsOrders.objects.create(title=product.title,description=product.descriptions,price=product.price,cart_id=cart.id,product_id=product.id)
            return Response({'message': 'اضافه شد'})
        else:
            return Response(data.errors)

class carts_remove(generics.CreateAPIView):
    serializer_class = OrdersSerializers


    def post(self, request, *args, **kwargs):
        data = OrdersSerializers(data=request.data)
        if data.is_valid():
            id = request.data.get('id',False)
            if id:
                user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
                token_info = Token.objects.filter(key=user_token).first()
                cart = ProductsCarts.objects.filter(user_id=token_info.user.id).first()
                order = ProductsOrders.objects.filter(id=id,product_id=data.validated_data['product'].id,payment_status=False).first()
                if order is not None:
                    order.delete()
                    return Response({'message': 'حذف شد'})
                else:
                    return Response({'message': 'error'})
            else:
                return Response({'id': 'این فیلد الزامی است'})
        else:
            return Response(data.errors)




class carts_list(generics.ListAPIView):
    serializer_class = OrdersSerializers

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        cart = get_object_or_404(ProductsCarts,user_id=token_info.user.id)
        return ProductsOrders.objects.filter(cart_id=cart.id,payment_status=False).all().order_by('id')