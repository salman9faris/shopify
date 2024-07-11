from django.shortcuts import render
from .models import Customer,Address

# Create your views here.
def profile(request):
    userprofile=Customer.objects.get(customer=request.user)
    address=Address.objects.filter(customer=request.user)
    
    print(userprofile)
    context={
        "userprofile":userprofile,
        "addresses":address
    }
    return render(request,"userprofile.html",context)