import django_filters

from .models import Products, Category

class ProductFilters(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ('category', 'product_name', 'uom',)

class CategoryFilters(django_filters.FilterSet):

    class Meta:
        model = Category
        fields = ('category_name',)
