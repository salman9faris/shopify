from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

from product.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.item
    
    def itemprice(self):
        return self.quantity*self.price
    
    def minquantity(self):
        return self.quantity
    
