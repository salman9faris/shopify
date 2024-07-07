from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    f_name=models.CharField("First name",max_length=50)
    l_name=models.CharField("Last name",max_length=50)
    mobile_number=models.CharField("Mobile number",max_length=80)
    email=models.CharField("email id",max_length=256)
   
    def __str__(self) -> str:
        return self.f_name


class Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    flat_no=models.CharField("flat/house no",max_length=80,blank=True)
    street=models.CharField(max_length = 150)
    area=models.CharField(max_length=150)
    district=models.CharField(max_length=160)
    state=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    zip_code=models.IntegerField("zip code")

    def __str__(self) -> str:
        return self.customer


    

