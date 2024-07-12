
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path("",views.cartpage,name='cartpage'),
 path("addtocart/<int:product_id>",views.addtocart,name="addtocart"),
 path("remove/<int:id>",views.removeitem,name="removeitem") ,
 path("checkout",views.checkout,name='checkout'),
 path("addquantiy/<int:id>",views.addquantiy,name="addquantiy"),
  path("minusquantiy/<int:id>",views.minusquantiy,name="minusquantiy")



]
