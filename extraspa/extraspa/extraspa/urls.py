from django.contrib import admin
from django.urls import path, include





admin.site.site_header = "Экстраспа Администрация"
admin.site.site_title = "Экстраспа Admin Portal"
admin.site.index_title = "Добро пожаловать на SPA ADMIN Portal!"

urlpatterns = [
    path('247admin/',admin.site.urls),
    path('', include('website.urls')),


]