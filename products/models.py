from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def add(self):
        self.save()

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    uom = models.CharField(max_length=200)

    def add(self):
        self.save()

    def __str__(self):
        return self.product_name
