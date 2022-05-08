from django.shortcuts import render,redirect
from .models import *

def derakhti_page(request):
    if request.user.is_authenticated:
        user = Users.objects.filter(id=request.user.id).first()
        if user.role == 'derakhti':
            return render(request,'derakhti/derakhti_page/derakhti_page.html')
        else:
            return redirect('Account:login_page')
    else:
        return redirect('Account:login_page')