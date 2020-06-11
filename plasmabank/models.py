from django.db import models

# Create your models here.
class Account(models.Model):
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    con_password = models.CharField(max_length=50)

class PlasmaDonor(models.Model):
    name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)