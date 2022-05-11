from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from random import choices
from string import ascii_lowercase,ascii_letters
from django.shortcuts import get_object_or_404
from extensions.derakhti.amount_purchased import amount_purchased

class contracts_add(generics.CreateAPIView):
    serializer_class = ContractsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = ContractsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            contract_check = Contracts.objects.filter(user_id=token_info.user.id).first()
            if contract_check is None:
                contract_create = Contracts.objects.create(user_id=token_info.user.id)
                return Response({'created': contract_create.jdate()})
            else:
                return Response({'message': 'قرار داد از قبل تایید شده'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)


class cards_add(generics.CreateAPIView):
    serializer_class = CardsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = CardsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            cards_check = Cards.objects.filter(user_id=token_info.user.id).first()
            if cards_check is None:
                data.save()
                data.instance.user = token_info.user
                data.save()
                return Response({'message': 'با موفقیت اضافه شد'})
            else:
                return Response({'message': ' از قبل اضافه شده'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)


class profile_update(generics.UpdateAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        data = UsersSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()
            data.update(user,data.validated_data)
            return Response({'message': 'بروز شد'})
        else:
            return Response(data.errors)


class place_user_buy(generics.CreateAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = MainUserSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            sub_categories_number = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
            if sub_categories_number != 12:
                user = Users.objects.filter(id=token_info.user.id).first()
                owner_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id).first()
                mainU = MainUser.objects.filter(user_id=token_info.user.id).first()

                if mainU is not None:
                    return Response({'message': 'کاربر قبلا  جایگاه انتخاب کرده است'})

                if owner_check is None:
                    return Response({'Owner': 'وجود ندارد'})
                else: pass

                mainU = MainUser.objects.filter(Owner=data.validated_data['Owner'].id).first()
                if data.validated_data['places'] == 1 and amount_purchased(token_info.user.id) >= 10005000:
                    data.save()



                elif  data.validated_data['r_or_l']  == True or  data.validated_data['r_or_l']  == False and data.validated_data['places'] in [2,3]:
                    if amount_purchased(token_info.user.id) >= 20010000 and data.validated_data['places'] == 2:
                        data.save()
                        data.instance.place = 2
                        if data.validated_data['r_or_l']:
                            Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                        else:
                            Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                        data.instance.r_or_l = data.validated_data['r_or_l']
                        data.save()



                    elif amount_purchased(token_info.user.id) >= 30015000 and data.validated_data['places'] == 3:
                        data.save()
                        data.instance.place = 3
                        Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                        Rusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                        data.instance.r_or_l = data.validated_data['r_or_l']
                        data.save()

                    else:
                        return Response({'message': 'موجودی شما کافی نیست '})

                elif amount_purchased(token_info.user.id) >= 70035000 and data.validated_data['places'] == 7:
                    data.save()
                    data.instance.places = 7
                    L1 = Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                    R1 = Rusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)


                    L2 = Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                    R2 = Rusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)

                    L3 = Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                    R3 = Rusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)

                    L4= Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)

                    Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)

                    data.instance.r_or_l = data.validated_data['r_or_l']
                    data.save()

                else:
                    return Response({'message': 'موجودی شما کافی نیست '})



                identifierـcode = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
                mainU_check = MainUser.objects.filter(identifierـcode=identifierـcode).first()
                if mainU_check is not None:
                    identifierـcode = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
                else: pass
                data.instance.user_id = token_info.user.id
                data.instance.identifierـcode = identifierـcode
                data.save()
                mainU = MainUser.objects.filter(user_id=token_info.user.id).first()
                mainU.payment_status = True
                mainU.save()

                return Response({'message': 'جایگاه خریداری شد'})
            else:
                return Response({'message': 'Owner جایگاه خالی ندارد'})


        else:
            return Response(data.errors)






class check_identifierـcode(generics.ListAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        identifierـcode = self.request.query_params.get('code',False)
        mainU = MainUser.objects.filter(identifierـcode=identifierـcode).first()
        if mainU is not None:
            return Response({'message': mainU.id})
        else:
            return Response({'message': 'کاربر وجود ندارد'})



class check_accses(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        contract = Contracts.objects.filter(user_id=token_info.user.id).first()
        card = Cards.objects.filter(user_id=token_info.user.id).first()
        user = Users.objects.filter(id=token_info.user.id).first()
        main_u = MainUser.objects.filter(user_id=token_info.user.id).first()

        if user.status == False:
            if contract is None:
                return Response({'message': 'خطا قرار داد فی ما برو تایید کنید'},status=status.HTTP_400_BAD_REQUEST)
            elif card is None:
                return Response({'message': 'خطا  اطلاعات حساب را اضافه  کنید'},status=status.HTTP_400_BAD_REQUEST)
            elif user.Book_or_buy_goods != True:
                return Response({'message': 'خطا  امتیاز خود  را انتخاب  کنید'}, status=status.HTTP_400_BAD_REQUEST)
            elif main_u is None:
                return Response({'message': 'خطا  جایگاه خود را انتخاب  کنید'},status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'message': 'حساب کاربر فعال شد'})

        else:
            return Response({'message': 'حساب کاربر فعال است'})




class select_points(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = SelectPointsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()
            user.Book_or_buy_goods = data.validated_data['Book_or_buy_goods']
            user.save()
            return Response({'message': 'بروزرسانی شد'})

        else:
            return Response(data.errors)




class sub_categories_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        main_u = MainUser.objects.filter(Owner_id=token_info.user.id).count()
        return Response({'number': main_u})




class place_active_right_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        r_user = Rusers.objects.filter(main_id=token_info.user.id,main__payment_status=True,main__r_or_l=True).count()
        return Response({'number': r_user})



class place_active_left_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        l_user = Lusers.objects.filter(main_id=token_info.user.id,main__payment_status=True,main__r_or_l=False).count()
        return Response({'number': l_user})



class place_reservation_right_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        r_user = Rusers.objects.filter(main_id=token_info.user.id,main__payment_status=False,main__r_or_l=False).count()
        return Response({'number': r_user})



class place_reservation_left_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        l_user = Lusers.objects.filter(main_id=token_info.user.id,main__payment_status=False,main__r_or_l=False).count()
        return Response({'number': l_user})


class orders_list(generics.ListAPIView):
    serializer_class = DerakhtiOrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductsOrders.objects.filter(shopper_id=token_info.user.id, payment_status=True).all().order_by('id')


class places_list(generics.ListAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        places = MainUser.objects.filter(Owner_id=token_info.user.id, payment_status=True).all()
        main = MainUser.objects.filter(user_id=token_info.user.id, payment_status=True).first()
        result = []
        result.append({'main': {'Owner': main.Owner.username,'user': main.user.username,'places': main.places,'r_or_l': main.r_or_l }})
        count = 0
        for p in places:
            result.append({'Owner': p.Owner.username,'user': p.user.username,'places': p.places,'r_or_l': p.r_or_l})
            count += 1

        if count != 15:
            while count < 15:
                result.append({'Owner': None,'user': None,'places': None,'r_or_l': None })
                count += 1

        return Response(result)

        #user = MainUser.objects.filter(Owner_id=token_info.user.id, payment_status=True).first()
        # R = Rusers.objects.filter(user_id=token_info.user.id,main__payment_status=True).all()
        # L = Lusers.objects.filter(user_id=token_info.user.id,main__payment_status=True).all()
        #
        # if user is not None:
        #     return Response({'info': {'main': {'owner': Owner.Owner.username,'user': user.Owner.username},'R': [{'Owner': r.main.Owner.username,'user': r.user.username} for r in R]} ,'L': [{'Owner': l.main.Owner.username,'user': l.user.username} for l in L], })
        #
        # else:
        #     return Response({'info': {'main': {'owner': Owner.Owner.username, 'user': Owner.user.username},'R': [{'Owner': r.main.Owner.username, 'user': r.user.username} for r in R]},'L': [{'Owner': l.main.Owner.username, 'user': l.user.username} for l in L], })


class places_list_filter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = self.request.query_params.get('username',False)
        result = []
        m = MainUser.objects.filter(payment_status=True,user__username=username).first()
        R = Rusers.objects.filter(user_id=m.user.id).all()
        L = Lusers.objects.filter(user_id=m.user.id).all()
        active_right = Rusers.objects.filter(main__Owner_id=m.user.id, main__payment_status=True).count()
        active_left = Lusers.objects.filter(main__Owner_id=m.user.id, main__payment_status=True).count()
        result.append( [{'R': {f'info': [{f'{r.id}': 'id','admin': r.main.admin.username,'owner': r.main.Owner.username,f'user': m.user.username,'active_right': active_right} for r in R]}},{'L' : {f'info': [{f'{l.id}': 'id','admin': l.main.admin.username,'owner': l.main.Owner.username,f'user': m.user.username,'active_right': active_right} for l in L]}}] )
        return Response(result)





class user_info(generics.ListAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        user = Users.objects.filter(id=token_info.user.id).first()
        card = Cards.objects.filter(user_id=token_info.user.id).first()
        if card is not None:
            return Response({'info': {'first_name': card.first_name,'last_name': card.last_name,'accountـnumber': card.accountـnumber,'shaba_number': card.shaba_number,'user_status': user.status,'mobile1': user.mobile1}})
        else:
            return Response({'info': 'empty'})









class admin_products_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProducts.objects.filter(user_id=token_info.user.id,status=True).all()


class admin_main_categories(generics.ListAPIView):
    serializer_class = DerakhtiProductMainCategoriesSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductMainCategories.objects.all()


class admin_sub_categories1(generics.ListAPIView):
    serializer_class = DerakhtiProductSubCategories_1Serializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        sub_categories1 = DerakhtiProductSubCategories_1.objects.filter(products__maincategories__id=id).distinct()

        return Response({'info': [{s1.id:s1.name}  for s1 in sub_categories1] })


class admin_sub_categories2(generics.ListAPIView):
    serializer_class = DerakhtiProductSubCategories_2Serializers
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        sub_categories2 = DerakhtiProductSubCategories_2.objects.filter(products__subCategories1__id=id).distinct()
        return Response({'info': [{s2.id:s2.name}  for s2 in sub_categories2] })



class admin_products_purchased(generics.ListAPIView):
    serializer_class = DerakhtiOrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductsOrders.objects.filter(product__user__id=token_info.user.id,payment_status=True).all()


class admin_products_comments_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductsComments.objects.filter(product__user__id=token_info.user.id).all()


class admin_products_add(generics.CreateAPIView):
    serializer_class = DerakhtiProductsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = DerakhtiProductsSerializers(data=request.data)
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
    serializer_class = DerakhtiProductsUpdateSerializers
    permission_classes = [IsAuthenticated]


    def update(self, request, *args, **kwargs):
        data = DerakhtiProductsUpdateSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            product = DerakhtiProducts.objects.filter(id=data.validated_data['id'],user_id=token_info.user.id).first()
            if product is not None:
                data.update(product,data.validated_data)
                return Response({'message': 'با موفقیت بروز شد'})
            else:
                return Response({'message': 'وجود ندارد'})
        else:
            return Response(data.errors)


class admin_products_delete(generics.CreateAPIView):
    serializer_class = DerakhtiProductsSerializers
    permission_classes = [IsAuthenticated]


    def post(self,request):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        product = DerakhtiProducts.objects.filter(id=id,user_id=token_info.user.id).first()
        if product is not None:
            product.delete()
            return Response({'message': 'حذف شد'})
        else:
            return Response({'message': 'وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)



class carts_add(generics.CreateAPIView):
    serializer_class = DerakhtiOrdersSerializers

    def post(self, request, *args, **kwargs):
        data = DerakhtiOrdersSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            cart = DerakhtiProductsCarts.objects.filter(user_id=token_info.user.id).first()
            if cart is None:
                cart_create = DerakhtiProductsCarts.objects.create(user_id=token_info.user.id)
            else: pass
            cart = DerakhtiProductsCarts.objects.filter(user_id=token_info.user.id).first()
            product = DerakhtiProducts.objects.filter(id=data.validated_data['product'].id).first()
            DerakhtiProductsOrders.objects.create(shopper_id=token_info.user.id,title=product.title,description=product.descriptions,price=product.price,cart_id=cart.id,product_id=product.id)
            return Response({'message': 'اضافه شد'})
        else:
            return Response(data.errors)

class carts_remove(generics.CreateAPIView):
    serializer_class = DerakhtiOrdersSerializers


    def post(self, request, *args, **kwargs):
        data = DerakhtiOrdersSerializers(data=request.data)
        if data.is_valid():
            id = request.data.get('id',False)
            if id:
                user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
                token_info = Token.objects.filter(key=user_token).first()
                cart = DerakhtiProductsCarts.objects.filter(user_id=token_info.user.id).first()
                order = DerakhtiProductsOrders.objects.filter(id=id,product_id=data.validated_data['product'].id,payment_status=False).first()
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
    serializer_class = DerakhtiOrdersSerializers

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        cart = get_object_or_404(DerakhtiProductsCarts,user_id=token_info.user.id)
        return DerakhtiProductsOrders.objects.filter(cart_id=cart.id,payment_status=False).all().order_by('id')




class products_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers

    def get_queryset(self):
        return DerakhtiProducts.objects.filter(status=True,vocher=False).all()

class products_list_vocher(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers

    def get_queryset(self):
        return DerakhtiProducts.objects.filter(status=True,vocher=True).all()


class products_comments_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsCommentsSerializers

    def get_queryset(self):
        product_id = self.request.query_params.get('id',False)
        return DerakhtiProductsComments.objects.filter(product_id=product_id,status=True).all()




class products_comments_add(generics.CreateAPIView):
    serializer_class = DerakhtiProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = DerakhtiProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            productComments_check = DerakhtiProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                DerakhtiProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=False).save()
                return Response({'message': 'دیدگاه ثبت شد'})
            else:
                return Response({"message": "کاربر قبلا برای این محصول دیدگاه ثبت کرده است"})
        else:
            return Response(data.errors)


class products_filter_maincategory_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return DerakhtiProducts.objects.filter(maincategories__id=id,status=True).all()

