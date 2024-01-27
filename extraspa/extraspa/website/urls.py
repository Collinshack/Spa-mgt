from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('phygenerate', views.physical_generate, name='phygenerate'),
    path('electric_sum', views.electric_sum, name='electric_sum'),
    path('electric_service', views.electric_service, name='electric_service'),
    path('qrdisplay', views.qrcode_sum, name='qrdisplay'),

]
