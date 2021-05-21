from django.urls import path
from .views import ProductCreateView,ProductListView,ProductDetailView,ProductUpdateView,UserProductListView,BidCreateView
app_name = 'pages'
urlpatterns = [
    path('',ProductListView.as_view(),name='product_list'),
    path('<int:id>/<slug:slug>/',ProductDetailView.as_view(),name='product_detail'),
    path('product/add/',ProductCreateView.as_view(),name='product_add'),
    path('<int:id>/<slug:slug>/edit/',ProductUpdateView.as_view(),name='product_edit'),
    path('product/myposts',UserProductListView.as_view(),name='myposts'),
    path('bid/add',BidCreateView.as_view(),name='bid_add'),

]
