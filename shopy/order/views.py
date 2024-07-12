from django.shortcuts import render,redirect

# Create your views here.
def orderpage(request):
    return render(request,"orderpage.html")



