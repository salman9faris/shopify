from django.contrib import admin
from .models import customer

class customerdetails(admin.ModelAdmin):
    list_display=("id","user","f_name","mobile_number","email","address")
    

# Register your models here.
admin.site.register(customer,customerdetails)