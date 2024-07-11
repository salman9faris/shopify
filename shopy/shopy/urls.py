
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('product.urls')),
    path("order/",include('order.urls')),
    path("cart/",include('cart.urls')),
    path("profile/",include('customers.urls')),
]
