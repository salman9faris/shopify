from django.contrib import admin
from .models import Customer,Address

class Customerdetails(admin.ModelAdmin):
    list_display=("id","user","f_name","mobile_number","email")

class Customeraddress(admin.ModelAdmin):
    list_display=("id","customer","flat_no","area","district","state","country","zip_code")
    

# Register your models here.
admin.site.register(Customer,Customerdetails)
admin.site.register(Address,Customeraddress)