from django.contrib import admin
from .models import Category, Products

my_models = [Category, Products]
admin.site.register(my_models)
