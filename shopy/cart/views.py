from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404

from customers.models import Address
from order.models import Coupon, shippingcharge

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
        return render(request,"cart.html",context)

def addtocart(request,product_id):
        product=Product.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(product=product,user=request.user,
                                                     price=product.discount_price,)
        cart_item.quantity+=1
        cart_item.save()
        return redirect(request.META['HTTP_REFERER'])


def removeitem(request,id):
        item=get_object_or_404(Cart, id=id)
        
        if item.user==request.user:
            item.delete()
            messages.success(request, "Item removed from your cart.")
        return redirect("cartpage")
def addquantiy(request,id):
        item=get_object_or_404(Cart, id=id)
        if item.user==request.user:
                if item.quantity<5:
                        print("pressed plus")
                        item.quantity+=1
                        item.save()
        return redirect("cartpage")

def minusquantiy(request,id):
        item=get_object_or_404(Cart, id=id)
        if item.user==request.user:
                if item.quantity>1:
                        item.quantity-=1
                        item.save()
        return redirect("cartpage")


def checkout(request):
        discount=0
        items=Cart.objects.filter(user=request.user)
        addresses=Address.objects.filter(customer=request.user)
        total_price=sum(item.quantity*item.price for item in items)
        charge=shippingcharge.objects.first()
        if total_price>charge.minimum_amount:
               shipping_charge=0
               total=total_price-int(discount)
        else:
             shipping_charge=charge.shipping_charge
             total=total_price+charge.shipping_charge-int(discount)
        if request.method=="POST" and "coupon-code" in request.POST:
                coupen_codes=request.POST.get("coupon-code")
                coupon=Coupon.objects.filter(coupon_code=coupen_codes)
                if coupon:
                        _coupon=Coupon.objects.get(coupon_code=coupen_codes)
                        discount=_coupon.coupon_amount
                        cost=total_price+charge.shipping_charge
                        if cost>int(discount):
                                total=cost-int(discount)
                                messages.success(request, f"valid coupon code, amount: {discount}")
                        else:
                                discount=0
                                messages.error(request, "invalid coupon code")
                else:
                        messages.error(request, "invalid coupon code")
        elif request.method=="POST" and "clear-code" in request.POST:
                discount=0
                total=total_price+charge.shipping_charge-int(discount)
                messages.success(request, "coupon cleared") 

        elif request.method=="POST" and "place-order" in request.POST:
                pass
        


                
           
        
       
        context={
            "items" : items,
            "addresses":addresses,
            "total_price":total_price,
            "shipping_charge":shipping_charge,
            "total":total,
            "discount":discount,
            
            
        }  
        return render(request,"checkout.html",context)
