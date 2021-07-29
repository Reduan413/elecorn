from django.db import models
from company.models import *


# Create your models here.

#Inventory Management

class Unit(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

class Category(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

class Sub_Category(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

class Brand(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

class Locator_Name(models.Model):
    name = models.CharField(max_length=100)

class Segment(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    code = models.CharField(max_length=8)
    part_no = models.CharField(max_length=50)
    # serial_no = models.CharField(max_length=50)
    market_name = models.CharField(max_length=50)
    model_no = models.CharField(max_length=50)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    segment_id = models.ForeignKey(Segment, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    description = models.TextField()
    # room_no = models.ForeignKey(Category, on_delete=models.CASCADE)
    # partition_no = models.ForeignKey(Category, on_delete=models.CASCADE)
    # rack_no = models.ForeignKey(Category, on_delete=models.CASCADE)
    # bin_no = models.ForeignKey(Category, on_delete=models.CASCADE)
    # box_no = models.ForeignKey(Category, on_delete=models.CASCADE)
    barcode_type = models.CharField(max_length=100)
    sku_no = models.CharField(max_length=100)
    alert_quantity = models.CharField(max_length=100)
    # image = models.CharField(max_length=100)
    narration = models.TextField()
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0.00)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0.00)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)



    # Warehouse Management

class Warehouse_Room(models.Model):
    name = models.CharField(max_length=100)

class Warehouse_Rack(models.Model):
    name = models.CharField(max_length=20)

class Warehouse_Bin(models.Model):
    name = models.CharField(max_length=20)

class Warehouse_Box(models.Model):
    name = models.CharField(max_length=20)

class Warehouse_Type(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

class Warehouse(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)