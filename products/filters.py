import django_filters as filters
from django_tables2 import SingleTableView
from .models import Products, Category

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Products
        fields = ['product_name', 'category', 'uom']

class CategoryFilter(filters.FilterSet):

    class Meta:
        model = Category
        fields = ['category_name']
