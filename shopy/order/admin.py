from django.contrib import admin
from order.models import Order,Ordereditem, shippingaddress



class orderadmin(admin.ModelAdmin):
    list_display=("id","customer","order_status","shipment_status","Payment_method","total_price","Payment_status")

class Ordereditemadmin(admin.ModelAdmin):
    list_display=("order_id","item","order","price","quantity")

class shippingadmin(admin.ModelAdmin):
    list_display=("id","customer","order","address")

# Register your models here.
admin.site.register(Order,orderadmin)
admin.site.register(Ordereditem,Ordereditemadmin)
admin.site.register(shippingaddress,shippingadmin)