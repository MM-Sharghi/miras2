from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated,IsTaksathiAdmin
from rest_framework.authtoken.models import Token
from .seralizers import *
from .models import ProductsOrders,ProductsCarts,Products
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from extensions.taksathi.day import day
from extensions.taksathi.week import week
from extensions.taksathi.month import month
from extensions.taksathi.year import year

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
            ProductsOrders.objects.create(shopper_id=token_info.user.id,title=product.title,description=product.descriptions,price=product.price,cart_id=cart.id,product_id=product.id)
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


class products_filter_maincategory_list(generics.ListAPIView):
    serializer_class = ProductsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return Products.objects.filter(maincategories__id=id,status=True).all()



#  Tak Sathi Admin

class admin_products_orders_day(generics.ListAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Response({'total_price': day(token_info.user.id)})

class admin_products_orders_week(generics.ListAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Response({'total_price': week(token_info.user.id)})

class admin_products_orders_month(generics.ListAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Response({'total_price': month(token_info.user.id)})

class admin_products_orders_year(generics.ListAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Response({'total_price': year(token_info.user.id)})

class admin_products_list(generics.ListAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Products.objects.filter(user_id=token_info.user.id,status=True).all()

class admin_products_purchased(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsTaksathiAdmin]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsOrders.objects.filter(product__user__id=token_info.user.id,payment_status=True).all()


class admin_products_comments_list(generics.ListAPIView):
    serializer_class = ProductsCommentsSerializers
    permission_classes = [IsTaksathiAdmin]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsComments.objects.filter(product__user__id=token_info.user.id).all()


class admin_products_add(generics.CreateAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]

    def post(self,request):
        data = ProductsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            data.save()
            data.instance.user = token_info.user
            data.save()

            return Response({'message': 'با موفقیت اضافه شد'})
        else:
            return Response(data.errors)


class admin_products_update(generics.UpdateAPIView):
    serializer_class = ProductsUpdateSerializers
    permission_classes = [IsTaksathiAdmin]


    def update(self, request, *args, **kwargs):
        data = ProductsUpdateSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            product = Products.objects.filter(id=data.validated_data['id'],user_id=token_info.user.id).first()
            if product is not None:
                data.update(product,data.validated_data)
                return Response({'message': 'با موفقیت بروز شد'})
            else:
                return Response({'message': 'وجود ندارد'})
        else:
            return Response(data.errors)


class admin_products_delete(generics.CreateAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsTaksathiAdmin]


    def post(self,request):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        product = Products.objects.filter(id=id,user_id=token_info.user.id).first()
        if product is not None:
            product.delete()
            return Response({'message': 'حذف شد'})
        else:
            return Response({'message': 'وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)

class admin_tikets_list(generics.ListAPIView):
    serializer_class = TiketSerializers
    permission_classes = [IsTaksathiAdmin]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Tiket.objects.filter(support_id=token_info.user.id).all()

class admin_tikets_filter(generics.ListAPIView):
    serializer_class = TiketSerializers
    permission_classes = [IsTaksathiAdmin]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Messages.objects.filter(tiket_id=id,support_id=token_info.user.id).all()



class admin_tikets_add(generics.CreateAPIView):
    serializer_class = MessagesSupportSerializers
    permission_classes = [IsTaksathiAdmin]

    def post(self,request):
        data = MessagesSupportSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            data.save()
            data.instance.support = token_info.user
            data.save()
            return Response({'message': 'با موفقیت اضافه شد'})
        else:
            return Response(data.errors)

class admin_tikets_update_status(generics.UpdateAPIView):
    serializer_class = TiketSupportUpdateStatusSerializers
    permission_classes = [IsTaksathiAdmin]

    def update(self, request, *args, **kwargs):
        data = TiketSupportUpdateStatusSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            if request.data.get('status'):
                pass
            else:
                return Response({'status': 'این فیلد الزامی است'})
            tiket = Tiket.objects.filter(id=data.validated_data['id'],user_id=data.validated_data['user']).first()
            if tiket is None:
                return Response({'message': 'اطلاعات وارد شده اشتباه است'})
            data.update(tiket,data.validated_data)
            return Response({'message': "با موفقیت بروز شد"})
        else:
            return Response(data.errors)





# End Tak Sathi Admin









class taksathi_panel_products_orders_list(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsOrders.objects.filter(shopper_id=token_info.user.id,payment_status=True).all().order_by('id')


class taksathi_panel_user_edit_profile(generics.UpdateAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        data = UserSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()
            data.update(user,data.validated_data)
            return Response({'message': 'ok'})
        else:
            return Response(data.errors)


class taksathi_panel_tikets_list(generics.ListAPIView):
    serializer_class = TiketSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Tiket.objects.filter(user_id=token_info.user.id).all()

class taksathi_panel_tikets_filter(generics.ListAPIView):
    serializer_class = TiketSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Messages.objects.filter(tiket_id=id,user_id=token_info.user.id).all()

class taksathi_panel_tikets_new(generics.CreateAPIView):
    serializer_class = TiketSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = TiketSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            data.save()
            data.instance.user = token_info.user
            data.save()
            return Response({'created': data.instance.id})
        else:
            return Response(data.errors)




class taksathi_panel_tikets_add(generics.CreateAPIView):
    serializer_class = MessagesUserSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = MessagesUserSerializers(data=request.data)
        if data.is_valid():
            if request.data.get('support'):
                pass
            else:
                return Response({'support': 'این مقدار الزامی است'})

            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            data.save()
            data.instance.support = token_info.user
            data.save()
            return Response({'message': 'با موفقیت اضافه شد'})
        else:
            return Response(data.errors)



