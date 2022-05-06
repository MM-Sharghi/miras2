from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsTaksathiAdmin
from rest_framework.authtoken.models import Token
from .seralizers import *
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

class products_comments_list(generics.ListAPIView):
    serializer_class = ProductsCommentsSerializers

    def get_queryset(self):
        product_id = self.request.query_params.get('id',False)
        return ProductsComments.objects.filter(product_id=product_id,status=True).all()




class products_comments_add(generics.CreateAPIView):
    serializer_class = ProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            productComments_check = ProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                ProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=False).save()
                return Response({'message': 'دیدگاه ثبت شد'})
            else:
                return Response({"message": "کاربر قبلا برای این محصول دیدگاه ثبت کرده است"})
        else:
            return Response(data.errors)


class products_add(generics.CreateAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def post(self,request):
        data = ProductsSerializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response({'message': 'با موفقیت اضافه شد'})
        else:
            return Response(data.errors)


class products_orders_list(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsOrders.objects.filter(payment_status=True).all().order_by('id')


class user_edit_profile(generics.UpdateAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]



    def post(self, request, *args, **kwargs):
        data = UserSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()
            data.update(user,data.validated_data)

            return Response({'message': 'ok'})
        else:
            return Response(data.errors)