from django.db import models
from django.utils import timezone
from django.conf import settings
from inventory.models import *
from authuser.models import *

# Create your models here.

class Incident_Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    # created_by = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, null=True)
    # updated_by = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField( auto_now=True, editable=False)

class Repair_Request(models.Model):
    code = models.CharField(max_length=12)
    date = models.DateField()
    device_name = models.CharField(max_length=100)
    part_no = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    incident_category = models.ForeignKey(Incident_Category, on_delete=models.CASCADE)
    details = models.TextField()
    person_name = models.CharField(max_length=255)
    primary_contact_no = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    narrition = models.TextField(null=True)
    status = models.CharField(max_length=50, blank=False, default="Pending")
    # created_by = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, null=True)
    # updated_by = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField( auto_now=True, editable=False)

class Repair(models.Model):
    item=models.ForeignKey(Repair_Request, on_delete=models.CASCADE, related_name="repair_item")
    engineer=models.ForeignKey(User, on_delete=models.CASCADE)
    remarks=models.CharField(max_length=255,)
    # created_by = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, null=True)
    # updated_by = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField( auto_now=True, editable=False)

class Repair_Comments(models.Model):
    item=models.ForeignKey(Repair, on_delete=models.CASCADE, related_name="repair_item")
    comments=models.TextField()
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    # updated_at = models.DateTimeField(auto_now=True, editable=False)


