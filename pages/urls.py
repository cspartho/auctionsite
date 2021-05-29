from django.urls import path
from .views import ProductCreateView,ProductListView,ProductDetailView,ProductUpdateView,UserProductListView,BidUpdateView
app_name = 'pages'
urlpatterns = [
    path('',ProductListView.as_view(),name='product_list'),
    path('<int:id>/<slug:slug>/',ProductDetailView.as_view(),name='product_detail'),
    path('product/add/',ProductCreateView.as_view(),name='product_add'),
    path('product/edit/<int:id>/<slug:slug>/',ProductUpdateView.as_view(),name='product_edit'),
    path('product/myposts',UserProductListView.as_view(),name='myposts'),
    path('bid/edit/<int:pk>',BidUpdateView.as_view(),name='bid_edit'),
]
