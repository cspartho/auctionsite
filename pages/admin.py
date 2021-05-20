from django.contrib import admin
from .models import Products,Auction
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display=["title","minimum_bid_price","date_posted","end_time",'created_by',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Products,ProductsAdmin)
admin.site.register(Auction)