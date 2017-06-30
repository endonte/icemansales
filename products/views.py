from django.shortcuts import render
from django.shortcuts import redirect
from django_tables2 import RequestConfig
from .models import Products, Category
from .tables import ProductTable, CategoryTable
from .forms import ProductForm, CategoryForm
from .filters import ProductFilter, CategoryFilter

def products(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('products')
    else:
        form = ProductForm()
        queryset = Products.objects.select_related().all()
        f = ProductFilter(request.GET, queryset=queryset)
        table = ProductTable(f.qs)
        RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(table)
    return render(request, 'products/products.html', {'table': table, 'filter': f, 'form': form})

def category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('category')
    else:
        form = CategoryForm()
        queryset = Category.objects.select_related().all()
        f = CategoryFilter(request.GET, queryset=queryset)
        table = CategoryTable(f.qs)
        RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(table)
    return render(request, 'products/category.html', {'table': table, 'filter': f, 'form': form})
