from django.contrib import admin
from product.models import Product,Category,Unit

#customize area

admin.site.site_header = " Shopy - enhance your style"
admin.site.index_title = " shopy - Admin"
admin.site.site_title = "enhance your style"

#display in admin

class Productadmin(admin.ModelAdmin):
    list_display=("id",'item',"category","orginal_price","disount_percentage","discount_price",)



# Register your models here.
admin.site.register(Product,Productadmin)
admin.site.register(Category)
admin.site.register(Unit)