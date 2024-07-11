from django.shortcuts import render,redirect

# Create your views here.
def orderpage(request):
    return render(request,"orderpage.html")


def addorder(request):
    
    return  redirect(request.META['HTTP_REFERER'])

