from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'category/', views.category, name='category'),
    url(r'products/', views.products, name='products'),
]
