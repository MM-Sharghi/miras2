from django.urls import path
from . import views

app_name = 'Taksathi'

urlpatterns = [
    path('products/',views.products_page,name='products_page'),
    path('products/detail/<int:id>/<str:slug>/',views.products_detail_page,name='products_detail_page'),
    path('tak-s-panel/',views.taksathi_panel_page,name='taksathi_panel_page'),
    path('tak-s-admin-panel/',views.taksathi_admin_panel_page,name='taksathi_admin_panel_page'),
    path('carts/',views.carts_page,name='carts_page'),
]
