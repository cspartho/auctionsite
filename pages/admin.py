from django.contrib import admin
from .models import Products,Bid
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display=["title","minimum_bid_price","date_posted","end_time",'created_by',]
    prepopulated_fields = {'slug': ('title',)}

class BidInline(admin.TabularInline):
    model = Bid

class BidAdmin(admin.ModelAdmin):
    inlines=[
        BidInline,
    ]
    llist_display=["title","minimum_bid_price","date_posted","end_time",'created_by',]

admin.site.register(Products,BidAdmin)
