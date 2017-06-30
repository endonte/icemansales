from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Products, Category
from .tables import ProductsTable

def category(request):
    categories = Category.objects.all().order_by('category_name')
    products.paginate(page=request.GET.get('page', 1), per_page=1)
    return render(request, 'products/category.html', {'categories': categories})

def products(request):
    products = ProductsTable(Products.objects.all().order_by('id'))
    RequestConfig(request, paginate={'per_page': 1}).configure(products)
    return render(request, 'products/products.html', {'products': products})
