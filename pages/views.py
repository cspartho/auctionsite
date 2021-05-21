from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.models import User
from .models import Products,Bid
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Create your views here.

class ProductListView(ListView):
    model = Products
    template_name ='product/list.html'
    context_object_name = 'products'
    paginate_by =5
    queryset = Products.objects.all()

class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Products
    template_name = 'product/detail.html'
    context_object_name='product'

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Products
    template_name ='product/product_add.html'
    fields =['title','image','description','minimum_bid_price','end_time']
    #success_url = reverse_lazy('product/list.html')

    #To add author of the posted itmes
    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Products
    fields = ['title','image','description','minimum_bid_price',]
    template_name ='product/product_update.html'
    
    #specific user can only update 
    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user


class UserProductListView(ListView):
    model = Products
    template_name ='user/user_post.html'
    context_object_name = 'products'
    paginate_by =5
    def get_queryset(self):
        queryset = Products.objects.filter(created_by=self.request.user)
        return queryset

class BidCreateView(CreateView):
    model = Bid
    template_name = 'bid/bid_add.html'
    fields=['bid_price']
    context_object_name = 'bidder'

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)