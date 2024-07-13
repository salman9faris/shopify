from django.contrib import admin
from cart.models import Cartitem,Cart



class cartadimn(admin.ModelAdmin):
    list_display=("id","user","total_price","discount_code","discount_amount","shipping_amount","total")

class cartitemadmin(admin.ModelAdmin):
    list_display=("id","user","product","price","quantity","total_price")

# Register your models here.
admin.site.register(Cartitem,cartitemadmin)
admin.site.register(Cart,cartadimn)