from django.urls import path
from .views import product_list,product_detail
app_name = 'pages'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:id>/<slug:slug>/',product_detail,name='product_detail'),

]
