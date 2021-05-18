from django.urls import path
from .views import product_list,product_detail
urlpatterns = [
    path('', product_list, name='home'),
]
