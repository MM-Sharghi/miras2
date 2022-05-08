from django.urls import path
from . import api_views

app_name = 'ApiDerakhti'

urlpatterns = [
    path('contracts-add/',api_views.contracts_add.as_view(),name='contracts_add'),
    path('cards-add/',api_views.cards_add.as_view(),name='cards_add'),
    path('profile-update/',api_views.profile_update.as_view(),name='profile_update'),
    path('place-user-buy/',api_views.place_user_buy.as_view(),name='place_user_buy'),
    path('check-identifier-code/',api_views.check_identifierـcode.as_view(),name='check_identifierـcode'),
    path('check-accses/',api_views.check_accses.as_view(),name='check_accses'),
    path('select-points/',api_views.select_points.as_view(),name='select_points'),
    path('sub-categories-number/',api_views.sub_categories_number.as_view(),name='sub_categories_number'),
    path('place-active-right-number/',api_views.place_active_right_number.as_view(),name='place_active_right_number'),
    path('place-active-left-number/',api_views.place_active_left_number.as_view(),name='place_active_left_number'),
    path('place-reservation-right-number/',api_views.place_reservation_right_number.as_view(),name='place_reservation_right_number'),
    path('place-reservation-left-number/',api_views.place_reservation_left_number.as_view(),name='place_reservation_left_number'),
    path('orders-list/',api_views.orders_list.as_view(),name='orders_list'),
    path('places-list/',api_views.places_list.as_view(),name='places_list'),
    path('places-list-filter/',api_views.places_list_filter.as_view(),name='places_list_filter'),
]