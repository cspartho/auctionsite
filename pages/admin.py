from django.contrib import admin
from .models import Products,Auction
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display=["title","minimum_bid_price","slug","date_posted",]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Products,ProductsAdmin)
admin.site.register(Auction)