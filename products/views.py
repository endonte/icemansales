from django.shortcuts import render

def category(request):
    return render(request, 'products/category.html', {})

def products(request):
    return render(request, 'products/products.html', {})
