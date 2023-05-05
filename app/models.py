from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(default="temp@temp.com")
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
