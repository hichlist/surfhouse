from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # mid_name = models.CharField(max_length=30, blank=True)

class Product(models.Model):
    product_name = models.CharField(max_length=60)
    product_size = models.CharField(max_length=60)
    product_material = models.CharField(max_length=60)
    product_wheels = models.CharField(max_length=60)
    product_bearings = models.CharField(max_length=60)
    product_prise = models.DecimalField(max_digits=10, decimal_places=2)