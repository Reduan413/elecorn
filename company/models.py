from django.db import models

# Create your models here.

class Company(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=100)
    address = models.TextField()
    license_no = models.CharField(max_length=50)


class Cost_Center(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name


class Department(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)


class UserInformation(models.Model):
    firstName = models.CharField(max_length=150) 
    lastName = models.CharField(max_length=150)
    email = models.CharField(max_length=50) 
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    company = models.ManyToManyField(Company)
