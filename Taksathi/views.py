from django.shortcuts import render,get_object_or_404
from .models import *
from rest_framework.authtoken.models import Token

def products_page(request):
    sliders = ProductsSliders.objects.all()
    maincategories1 = ProductMainCategories.objects.filter(products__status=True).all()[:6]
    maincategories2 = ProductMainCategories.objects.filter(products__status=True).order_by('-id').all()[:6]
    products = Products.objects.filter(status=True).all()
    context = {
        'products': products,
        'sliders': sliders,
        'maincategories1': maincategories1,
        'maincategories2': maincategories2,
    }
    return render(request,'Taksathi/products_page/products_page.html',context)


def products_detail_page(request,id,slug):
    product = get_object_or_404(Products,id=id,slug=slug)
    similars = Products.objects.filter(maincategories__id__in=[p.id for p in product.maincategories.all()])
    user_token = Token.objects.filter(user_id=request.user.id).first()
    context = {
        'product': product,
        'similars': similars,
        'user_token': user_token,
    }
    return render(request,'Taksathi/products_detail_page/products_detail_page.html',context)

def taksathi_panel_page(request):
    context = {

    }
    return render(request,'Taksathi/taksathi_panel_page/taksathi_panel_page.html',context)


def carts_page(request):
    context = {

    }
    return render(request,'Taksathi/carts/shoping-bag.html',context)


