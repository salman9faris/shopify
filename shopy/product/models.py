from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category=models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.category

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    unit=models.CharField(max_length=64,unique=True)
    def __str__(self):
        return self.unit


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    item=models.CharField(max_length=256)
    description=models.CharField(max_length=256)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default="")
    orginal_price=models.CharField(max_length=256)
    disount_percentage=models.IntegerField()
    discount_price=models.CharField(max_length=256)
    unit=models.ForeignKey(Unit,max_length=256,on_delete=models.CASCADE)
    max_quantity=models.CharField(max_length=256)
    thumbnail=models.CharField(max_length=256)
    image=models.ImageField(upload_to="product", max_length=400,blank=True)
    
   
   

    def __str__(self):
        return self.item
    



   
