from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404

from customers.models import Address

from .models import Cart
from product.models import Product

# Create your views here.

def cartpage(request):
        items=Cart.objects.filter(user=request.user)
        addresses=Address.objects.filter(customer=request.user)
        total_price=sum(item.quantity*item.price for item in items)
        
        context={
            "items" : items,
            "total_price":total_price,
            "addresses":addresses,
        }  
        return render(request,"cartpage.html",context)

def addtocart(request,product_id):
        product=Product.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(product=product,user=request.user,
                                                     price=product.discount_price,)
        cart_item.quantity+=1
        cart_item.save()
        return redirect(request.META['HTTP_REFERER'])


def removeitem(request,id):
        item=get_object_or_404(Cart, id=id)
        print(item.user)
        if item.user==request.user:
            item.delete()
            messages.success(request, "Item removed from your cart.")
        return redirect("cartpage")


def checkout(request):
    return render(request,"checkout.html")