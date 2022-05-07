from django.shortcuts import render
from .models import *

def derakhti_page(request):
    ruser = Rusers.objects.filter(main__user__id=2).all()
    print(ruser)

