from django.shortcuts import render
from django.contrib import messages
from Users.models import Users
from django.contrib.auth import login,authenticate
from .forms import *

def register_page(request):
    if request.method == "POST":
        form = AccountRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            user = Users.objects.filter(username=form.cleaned_data['username']).first()
            login(request,user)

        else:
            context = {
                'form': form,
            }
            messages.error(request, form.errors)
            return render(request, 'Account/register_page/register_page.html',context)
    return render(request,'Account/register_page/register_page.html')




def login_page(request):
    if request.method == "POST":
        user = Users.objects.filter(username=request.POST.get('username'),password=request.POST.get('password')).first()
        if user is not None:
            login(request,user)
        else:
            messages.error(request, 'اطلاعات اشتباه است')
            return render(request, 'Account/login_page/login_page.html')

    return render(request,'Account/login_page/login_page.html')
