from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




admin.site.site_header = "Экстраспа Administration"
admin.site.site_title = "Экстраспа Admin Portal"
admin.site.index_title = "Welcome to SPA ADMIN Portal"

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('website.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

