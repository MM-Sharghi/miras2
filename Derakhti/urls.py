from django.urls import path
from . import views

app_name = 'Derakhti'

urlpatterns = [
    path('', views.derakhti_page,name='derakhti_page'),
]