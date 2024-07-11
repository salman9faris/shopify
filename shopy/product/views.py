from django.shortcuts import render
from .models import Product
# Create your views here.

def homepage(request):
    return render(request,"index.html")
def allproduct(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"product.html",context)
def blogpage(request):
    return render(request,"blogpage.html")


def contactpage(request):
    return render(request,"contact.html")

def aboutpage(request):
    return render(request,"about.html")

def productpage(request):
    return render(request,"productdetail.html")

