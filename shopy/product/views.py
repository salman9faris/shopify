from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"index.html")

def cartpage(request):
    return render(request,"cartpage.html")

def allproduct(request):
    return render(request,"product.html")
def blogpage(request):
    return render(request,"blog_list.html")


def contactpage(request):
    return render(request,"contact.html")



def aboutpage(request):
    return render(request,"about.html")