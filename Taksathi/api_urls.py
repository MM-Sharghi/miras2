from django.urls import path
from . import api_views

app_name = 'ApiTaksathi'

urlpatterns = [
    path('carts/carts-add/',api_views.carts_add.as_view(),name='carts_add'),
    path('carts/carts-remove/',api_views.carts_remove.as_view(),name='carts_add'),
    path('carts/carts-list/',api_views.carts_list.as_view(),name='carts_list'),
]