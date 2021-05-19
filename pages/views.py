from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView

from .models import Products,Auction
from django.urls import reverse_lazy

# Create your views here.

class ProductListView(ListView):
    model = Products
    template_name ='product/list.html'
    context_object_name = 'products'
    paginate_by =5
    queryset = Products.objects.all()

class ProductDetailView(DetailView):
    model = Products
    template_name = 'product/detail.html'
    context_object_name='product'

class ProductCreateView(CreateView):
    model = Products
    template_name ='product/product_add.html'
    fields =['title','image','description','minimum_bid_price','end_time']
    #success_url = reverse_lazy('product/list.html')

class ProductUpdateView(UpdateView):
    model = Products
    fields = ['title','image','description','minimum_bid_price']