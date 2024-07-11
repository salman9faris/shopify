from datetime import timezone
from django.db import models
from product.models import Product
from cart.models import Cart
from customers.models import Address, Customer

# Create your models here.
order_status=[
       
        ("ORDERED","Ordered"),
        ("Failed","Failed"),
        ("CANCELLED","Cancelled"),
        ("COMPLETED","Completed"),

    ]

Payment_method=[
   ("Failed","Failed"),
        ("COD","COD"),
        ("Debit/Credit card","Debit/Credit card"),  
        ("Net banking","Net Banking")
    ]
Payment_status=[
        ("paid","Paid"),
        ("Not paid","Not paid"),  
        ("Failed","Failed")
    ]

shipment_status=[
    ("Preparing","Preparing"),
    ("SHIPPED","Shipped"),
    ("IN-TRANSIT","In-Transit"),
    ("DELIVERED","Delivered")
]
logistic_partner=[
    ("fed-ex","Fed-ex"),
    ("e-kart","e-kart")

 ]

    
class Order(models.Model): 
    id = models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    order_status=models.CharField(choices=order_status,default="ORDERED",max_length=80)
    Payment_method=models.CharField(choices=Payment_method,max_length=80)
    Payment_status=models.CharField(choices=Payment_status,max_length=80)
    shipment_awb=models.CharField(max_length=256,blank=True,default="")
    logistic_partner=models.CharField(choices=logistic_partner,max_length=80,blank=True)
    shipment_status=models.CharField(choices=shipment_status,max_length=80,default="Preparing")

    def __str__(self):
        return self.customer_name


class Ordereditem(models.Model):
    id = models.AutoField(primary_key=True)
    item=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    date_added=models.DateTimeField(auto_now_add=True)

class shippingaddress(models.Model):
    id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.address

   