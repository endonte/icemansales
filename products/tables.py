import django_tables2 as tables
from .models import Products, Category

class ProductsTable(tables.Table):
    class Meta:
        model = Products
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
