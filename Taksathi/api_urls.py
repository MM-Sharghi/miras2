from django.urls import path
from . import api_views

app_name = 'ApiTaksathi'

urlpatterns = [
    path('carts/carts-add/',api_views.carts_add.as_view(),name='carts_add'),
    path('carts/carts-remove/',api_views.carts_remove.as_view(),name='carts_add'),
    path('carts/carts-list/',api_views.carts_list.as_view(),name='carts_list'),
    path('products/products-comments-add/', api_views.products_comments_add.as_view(), name='products_comments_add'),
    path('products/products-comments-list/', api_views.products_comments_list.as_view(), name='products_comments_list'),
    path('products/products-add/', api_views.products_add.as_view(), name='products_add'),
    path('products/products-orders-list/', api_views.products_orders_list.as_view(), name='products_orders_list'),
    path('user/user-edit-profile/', api_views.user_edit_profile.as_view(), name='user_edit_profile'),
]