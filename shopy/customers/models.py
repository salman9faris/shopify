from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    f_name=models.CharField("first name",max_length=50)
    l_name=models.CharField("first name",max_length=50)
    mobile_number=models.CharField("mobile number",max_length=80)
    email=models.CharField(max_length=256)
    address=models.CharField(max_length=256,blank=True)


    def __str__(self) -> str:
        return self.f_name

