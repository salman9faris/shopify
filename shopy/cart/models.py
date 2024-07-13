from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

from product.models import Product



class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    total_price=models.FloatField(default=0)
    discount_code=models.CharField(max_length=25,default=0)
    discount_amount=models.PositiveIntegerField(default=0)
    shipping_amount=models.PositiveBigIntegerField(default=0)
    total=models.FloatField(default=0)

    def grandtotal(self):
        return self.total_price-int(self.discount_amount)
 
   


# Create your models here.
class Cartitem(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,)
    price=models.FloatField()
    quantity=models.PositiveIntegerField(default=0)
    total_price=models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.item
    
    def itemprice(self):
        return self.quantity*self.price
    
    def minquantity(self):
        return self.quantity
    
    def total(self):
        return self.quantity*self.price
    

    



  