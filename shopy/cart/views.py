from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404

from customers.models import Address


from .models import Cartitem,Cart
from product.models import Product

# Create your views here.

def cartpage(request):
        try:
                items=Cartitem.objects.filter(user=request.user)
                new_cart=Cart.objects.get(user=request.user)
                total_price=sum(item.quantity*item.price for item in items)
                new_cart.total_price=total_price
                grand_total=new_cart.grandtotal()
                new_cart.save()
                context={
                "items" : items,
                "total_price":total_price,
                
                "discount_amount":new_cart.discount_amount,
                "total":grand_total
                
                }  
                return render(request,"cart.html",context)
        except:
                return render(request,"cart.html")
                

def addtocart(request,product_id):
        product=Product.objects.get(id=product_id)
        new_cart,created=Cart.objects.get_or_create(user=request.user,)
        cart_item,created=Cartitem.objects.get_or_create(product=product,user=request.user,
                                                         cart=new_cart,
                                                     price=product.discount_price,total_price=product.discount_price) 
        cart_item.quantity+=1
        new_cart.save()
        cart_item.save()
        return redirect(request.META['HTTP_REFERER'])


def removeitem(request,id):
        item=get_object_or_404(Cartitem, id=id)
       
        if item.user==request.user:
            item.delete()
           
            messages.success(request, "Item removed from your cart.")
        return redirect("cartpage")
def addquantiy(request,id):
        item=get_object_or_404(Cartitem, id=id)
        if item.user==request.user:
                if item.quantity<5:
                        print("pressed plus")
                        item.quantity+=1
                        item.total_price=item.quantity*item.price
                        item.save()
                        
                       
                        
        return redirect("cartpage")

def minusquantiy(request,id):
        item=get_object_or_404(Cartitem, id=id)
        if item.user==request.user:
                if item.quantity>1:
                        item.quantity-=1
                        item.total_price=item.quantity*item.price
                        item.save()
        return redirect("cartpage")

