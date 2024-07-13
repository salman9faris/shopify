from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404

from customers.models import Address
from order.models import Coupon, shippingcharge,Order,Ordereditem

from cart.models import Cartitem,Cart
from customers.models import Customer
from product.models import Product

# Create your views here.
def orderpage(request):
    return render(request,"orderpage.html")




def checkout(request):
        items=Cartitem.objects.filter(user=request.user)
        addresses=Address.objects.filter(customer=request.user)
        total_price=sum(item.quantity*item.price for item in items)
        charge=shippingcharge.objects.first()
        cart=Cart.objects.get(user=request.user)
        discount=cart.discount_amount
        if charge.minimum_amount:
                if total_price<charge.minimum_amount and total_price>0:
                        cart.shipping_amount=charge.shipping_charge
                        cart.total=total_price+charge.shipping_charge-int(discount)
                        cart.save()
                else:
                        cart.shipping_amount=0
                        cart.total=total_price-int(discount)
                        cart.save()
             
        if request.method=="POST" and "coupon-code" in request.POST:
                coupen_codes=request.POST.get("coupon-code")
                coupon=Coupon.objects.filter(coupon_code=coupen_codes)
                if coupon:
                        coupons=Coupon.objects.get(coupon_code=coupen_codes)
                        discount=coupons.coupon_amount
                        code=coupons.coupon_code
                        cost=total_price+cart.shipping_amount
                        if cost>int(discount):
                                cart.discount_amount=discount
                                cart.discount_code=code
                                cart.total=cost-int(discount)
                                cart.save()
                                messages.success(request, f"valid coupon code, amount: {discount}")
                        else:
                                discount=0
                                messages.error(request, "invalid coupon code")
                else:
                        messages.error(request, "invalid coupon code")
        elif request.method=="POST" and "clear-code" in request.POST:
                
                cart.discount_amount=0
                cart.discount_code=0
                cart.total=total_price+cart.shipping_amount-cart.discount_amount
                cart.save()
                messages.success(request, "coupon cleared") 

        elif request.method=="POST" and "place-order" in request.POST:
                neworder = Order.objects.create(
                customer=request.user,
                total_price=cart.total,
                discount_coupon=cart.discount_code,
                discount_amount=cart.discount_amount)
                cartitems=Cartitem.objects.filter(user=request.user)
                neworder.save()  
                for cartitem in cartitems :
                       
                       Ordereditem.objects.create(
                        item=cartitem.product,
                        order=neworder,
                        quantity=cartitem.quantity,
                        price=cartitem.total_price,
                )
                Cartitem.objects.filter(user=request.user).delete()
                Cart.objects.filter(user=request.user).delete()
                       
                
        context={
            "items" : items,
            "addresses":addresses,
            "total_price":total_price,
            "shipping_charge":cart.shipping_amount,
            "total":cart.total,
            "discount":cart.discount_amount,
            
            
        }  
        return render(request,"checkout.html",context)
