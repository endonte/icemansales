import django_tables2 as tables
from .models import Products, Category

class ProductTable(tables.Table):
    category = tables.Column(accessor='category.category_name')
    class Meta:
        model = Products
        # add class="paleblue" to <table> tag
#        attrs = {'class': 'paleblue'}

class CategoryTable(tables.Table):
    class Meta:
        model = Category
