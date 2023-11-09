from django.contrib import admin
from .models import Promotion, Collection, Product, Customer, Order, OrderItem, Address, Cart, CartItem

admin.site.register(Promotion)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)

