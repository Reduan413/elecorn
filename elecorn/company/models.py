from django.db import models

# Create your models here.

class Company_Manager(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    contact_no = models.CharField(max_length=250)
    address = models.TextField()
    license_no = models.CharField(max_length=20)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)


class Cost_Center(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company_Manager, on_delete=models.CASCADE)
    address = models.TextField()
    email = models.CharField(max_length=250)
    contact_no = models.CharField(max_length=250)
    remarks = models.TextField()
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)


class Department(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company_Manager, on_delete=models.CASCADE)
    remarks = models.TextField()
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)


class Unit_Manager(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100, )
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    
