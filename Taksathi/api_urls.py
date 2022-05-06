from django.urls import path
from . import api_views

app_name = 'ApiTaksathi'

urlpatterns = [
    path('carts/carts-add/',api_views.carts_add.as_view(),name='carts_add'),
    path('carts/carts-remove/',api_views.carts_remove.as_view(),name='carts_add'),
    path('carts/carts-list/',api_views.carts_list.as_view(),name='carts_list'),

    # Api Products
    path('products/products-comments-add/', api_views.products_comments_add.as_view(), name='products_comments_add'),
    path('products/products-comments-list/', api_views.products_comments_list.as_view(), name='products_comments_list'),
    path('products/products-filter-maincategory-list/', api_views.products_filter_maincategory_list.as_view(), name='products_filter_maincategory_list'),


    # Api panel tak sathi
    path('tak-s-panel/products/products-orders-list/', api_views.taksathi_panel_products_orders_list.as_view(), name='products_orders_list'),
    path('tak-s-panel/user/user-edit-profile/', api_views.taksathi_panel_user_edit_profile.as_view(), name='user_edit_profile'),
    path('tak-s-panel/tikets/tikets-add/', api_views.taksathi_panel_tikets_add.as_view(), name='taksathi_panel_tikets_add'),
    path('tak-s-panel/tikets/tikets-new/', api_views.taksathi_panel_tikets_new.as_view(), name='taksathi_panel_tikets_new'),

    # Api panel admin tak sathi
    path('products/products-add/', api_views.products_add.as_view(), name='products_add'),
    path('tikets/tikets-add/', api_views.tikets_add.as_view(), name='tikets_add'),
    path('tikets/tikets-update-status/', api_views.tikets_update_status.as_view(), name='tikets_update_status'),


]