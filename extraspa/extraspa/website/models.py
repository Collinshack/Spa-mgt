from django.db import models
import random

def foo():
    return str(random.randint(99999,999999))
# Create your models here.

class ElectGen(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    service = models.CharField(max_length = 30)
    value = models.CharField(max_length = 30)
    amount = models.CharField(max_length = 30)
    uniquec = models.CharField(max_length=30)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

class PaperGen(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    unique = models.CharField(max_length=30)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")



