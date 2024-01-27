from django.contrib import admin
from .models import ElectGen, PaperGen

# Register your models here.
admin.site.register(PaperGen)
admin.site.register(ElectGen)
