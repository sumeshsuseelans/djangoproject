from django.contrib import admin
from .models import Items
from .models import userComments

admin.site.register(Items)
admin.site.register(userComments)