from django.db import models


from product.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=256)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,)
    quantity=models.IntegerField()
    price=models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.item