
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path("",views.homepage,name="homepage"),
    path("",views.orderpage,name='orderpage'),
    path("checkout",views.checkout,name='checkout'),

]
