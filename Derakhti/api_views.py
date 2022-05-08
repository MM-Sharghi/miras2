from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from random import choices
from string import ascii_lowercase,ascii_letters
from Taksathi.models import ProductsOrders
from Taksathi.seralizers import OrdersSerializers
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
            if amount_purchased(token_info.user.id) >= 20010000:
                sub_categories_number = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
                if sub_categories_number != 12:
                    user = Users.objects.filter(id=token_info.user.id).first()
                    owner_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id).first()
                    mainU = MainUser.objects.filter(user_id=token_info.user.id).first()

                    if mainU is not None:
                        return Response({'message': 'کاربر قبلا انتخاب کرده است'})

                    if owner_check is None:
                        return Response({'Owner': 'وجود ندارد'})
                    else: pass

                    mainU = MainUser.objects.filter(Owner=data.validated_data['Owner'].id).first()
                    if data.validated_data['places'] == 1 and amount_purchased(token_info.user.id) >= 10005000:
                        # print('chi hs')
                        # data.save()
                        return Response({'message': 'موجودی شما کافی نیست '})


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
                            data.instance.place = 3
                            if data.validated_data['r_or_l']:
                                Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                            else:
                                Lusers.objects.create(main_id=mainU.id, user_id=token_info.user.id)
                            data.instance.r_or_l = data.validated_data['r_or_l']
                            data.save()
                        else:
                            return Response({'message': 'موجودی شما کافی نیست '})
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

                    return Response({'message': 'اضافه شد'})
                else:
                    return Response({'message': 'Owner جایگاه خالی ندارد'})

            else:
                return Response({'message': 'موجودی شما کافی نیست '})
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
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsOrders.objects.filter(shopper_id=token_info.user.id, payment_status=True).all().order_by('id')


class places_list(generics.ListAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return MainUser.objects.filter(Owner_id=token_info.user.id, payment_status=True).all().order_by('id')

