from django.db import models
from django.contrib.auth.models import User
import random

# def foo():
#     return str(random.randint(99999,999999))

class Spa(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    admin = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='spa_admin', blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.value}₽"

class ElectronicCardSum(models.Model):
    STATUS_CHOICES = [
        ('Активен', 'Активен'),
        ('Потрачен', 'Потрачен'),
    ]
    TYPE_CHOICES = [
        ('service', 'Service'),
        ('sum', 'Sum'),
    ]
    spa = models.ForeignKey(Spa, on_delete=models.SET_NULL, related_name='elect_gens_sum', null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    type = models.CharField(choices=TYPE_CHOICES, default='sum', max_length=10)
    amount = models.IntegerField()
    uniquec = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Активен')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.amount == 0:
            self.status = 'Потрачен'
        super().save(*args, **kwargs)

class ElectronicCardService(models.Model):

    STATUS_CHOICES = [
        ('Активен', 'Активен'),
        ('Потрачен', 'Потрачен'),
    ]
    TYPE_CHOICES = [
        ('service', 'Service'),
        ('sum', 'Sum'),
    ]

    spa = models.ForeignKey(Spa, on_delete=models.SET_NULL, related_name='elect_gens_service', null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    type = models.CharField(choices=TYPE_CHOICES, default='service', max_length=10)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='elect_gens_service', blank=True, null=True)
    purchased_frequency = models.IntegerField()
    uniquec = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Активен')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.purchased_frequency == 0:
            self.status = 'Потрачен'
        super().save(*args, **kwargs)
    
    @property
    def service_value(self):
        if self.service:
            return self.service.value
        return None




    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.purchased_frequency == 0:
            self.status = 'Потрачен'
        super().save(*args, **kwargs)


class PhysicalCardService(models.Model):
    STATUS_CHOICES = [
        ('Активен', 'Активен'),
        ('Потрачен', 'Потрачен'),
    ]
    TYPE_CHOICES = [
        ('service', 'Service'),
        ('sum', 'Sum'),
    ]
    spa = models.ForeignKey(Spa, on_delete=models.SET_NULL, related_name='paper_gens_service', null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True, null=True)
    amount = models.IntegerField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    uniquec = models.CharField(max_length=30)
    type = models.CharField(choices=TYPE_CHOICES, default='service', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Активен')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.amount == 0:
            self.status = 'Потрачен'
        super().save(*args, **kwargs)

    @property
    def service_value(self):
        if self.service:
            return self.service.value
        return None