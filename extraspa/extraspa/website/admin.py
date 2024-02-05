from django.contrib import admin
from .models import Spa, Service, ElectronicCardSum, ElectronicCardService, PhysicalCardSum, PhysicalCardService




class SpaAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_phone', 'contact_email', 'admin')
    search_fields = ['name', 'admin']
    list_filter = ['location']

class ElectronicCardSumAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'type', 'amount', 'uniquec', 'status', 'created_at')
    search_fields = ['first_name', 'last_name', 'phone', 'type', 'uniquec', 'status', 'created_at']
    list_filter = ['amount', 'status', 'created_at']

class ElectronicCardServiceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'type', 'service', 'purchased_frequency', 'uniquec', 'status', 'created_at')
    search_fields = ['first_name', 'last_name', 'phone', 'type', 'uniquec', 'status', 'created_at']
    list_filter = ['service', 'type', 'status','created_at' ]

class PhysicalCardSumAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'type', 'amount', 'uniquec', 'status', 'created_at')
    search_fields = ['first_name', 'last_name', 'phone', 'type', 'uniquec', 'status', 'created_at']
    list_filter = ['amount', 'status', 'created_at']
    

class PhysicalCardServiceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'type', 'service', 'purchased_frequency', 'uniquec', 'status', 'created_at')
    search_fields = ['first_name', 'last_name', 'phone', 'type', 'uniquec', 'status', 'created_at']
    list_filter = ['service', 'type', 'status','created_at' ]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ['name', 'value']

admin.site.register(Spa, SpaAdmin)
admin.site.register(ElectronicCardSum, ElectronicCardSumAdmin)
admin.site.register(ElectronicCardService, ElectronicCardServiceAdmin)
admin.site.register(PhysicalCardSum, PhysicalCardSumAdmin)
admin.site.register(PhysicalCardService, PhysicalCardServiceAdmin)
admin.site.register(Service, ServiceAdmin)
