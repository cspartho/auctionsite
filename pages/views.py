from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from .models import Products,Auction
# Create your views here.



def product_list(request):
    products = Products.objects.all()

    return render(request,'product/list.html',{'products':products})

def product_detail(request,id,slug):
    product = get_object_or_404(Products,id=id,slug=slug)

    return render(request,'product/detail.html',{'products':products})