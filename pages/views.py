from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Products, Bid
from django.urls import reverse_lazy, reverse
from .forms import BidForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class ProductListView(ListView):
    model = Products
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 5
    queryset = Products.objects.all()


class ProductDetailView(FormMixin, DetailView):
    model = Products
    form_class = BidForm
    template_name = 'product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bidder'] = Bid.objects.all().order_by('-bid_price').first()
        context['bid'] = Bid.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.bid_item_id = self.object.pk
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pages:product_detail', kwargs={'id': self.object.pk, 'slug': self.object.slug})


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = 'product/product_add.html'
    fields = ['title', 'image', 'description', 'minimum_bid_price', 'end_time']
    #success_url = reverse_lazy('product/list.html')

    # To add author of the posted itmes
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Products
    fields = ['title', 'image', 'description', 'minimum_bid_price', 'end_time']
    template_name = 'product/product_update.html'

    # specific user can only update
    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user


class UserProductListView(ListView):
    model = Products
    template_name = 'user/user_post.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = Products.objects.filter(created_by=self.request.user)
        return queryset


class BidUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bid
    fields = ['bid_price', ]
    template_name = 'bid/bid_edit.html'

    # specific user can only update
    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user

