from django.shortcuts import render
from django.shortcuts import redirect
from django_tables2 import RequestConfig
from .models import Products, Category
from .tables import ProductTable, CategoryTable
from .forms import ProductForm, CategoryForm

#def category(request):
#    form = CategoryForm()
#    categories = CategoryTable(Category.objects.all().order_by('category_name'))
#    RequestConfig(request, paginate={'per_page': 25}).configure(categories)
#    return render(request, 'products/category.html', {'categories': categories, 'form': form})

def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('products')
    else:
        form = ProductForm()
        products_list = ProductTable(Products.objects.all().order_by('product_name'))
        RequestConfig(request, paginate={'per_page': 25}).configure(products_list)
    return render(request, 'products/products.html', {'products_list': products_list, 'form': form})

def category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('category')
    else:
        form = CategoryForm()
        categories = CategoryTable(Category.objects.all().order_by('category_name'))
        RequestConfig(request, paginate={'per_page': 25}).configure(categories)
    return render(request, 'products/category.html', {'categories': categories, 'form': form})
