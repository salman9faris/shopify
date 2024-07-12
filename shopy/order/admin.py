from django.contrib import admin
from order.models import Order,Ordereditem,Coupon,shippingaddress,shippingcharge

class orderadmin(admin.ModelAdmin):
    list_display=("id","customer","order_status","shipment_status","Payment_method","total_price","discount_coupon","discount_amount","Payment_status")

class Ordereditemadmin(admin.ModelAdmin):
    list_display=("order_id","item","order","price","quantity")

class shippingadmin(admin.ModelAdmin):
    list_display=("id","customer","order","address")

class shippingchargeadmin(admin.ModelAdmin):
    list_display=("id","shipping_charge","minimum_amount")
    
class couponadmin(admin.ModelAdmin):
    list_display=("id","coupon_code","coupon_amount")

# Register your models here.
admin.site.register(Order,orderadmin)
admin.site.register(Ordereditem,Ordereditemadmin)
admin.site.register(shippingaddress,shippingadmin)
admin.site.register(shippingcharge,shippingchargeadmin)
admin.site.register(Coupon,couponadmin)