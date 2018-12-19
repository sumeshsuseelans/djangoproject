from django.contrib import admin
from .models import Register
from .models import Cart
from .models import Items
from .models import ShippingAddress
from .models import OrderNumber

admin.site.register(Register)
admin.site.register(Cart)
admin.site.register(Items)
admin.site.register(ShippingAddress)
admin.site.register(OrderNumber)