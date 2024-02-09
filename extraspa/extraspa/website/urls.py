from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('records/', views.records, name='records'),
    path('search-electronic-card-sum/', views.search_electronic_card_sum, name='search_electronic_card_sum'),
    path('search-electronic-card-service/', views.search_electronic_card_service, name='search_electronic_card_service'),
   
    path('search-physical-card-service/', views.search_physical_card_service, name='search_physical_card_service'),


    
    path('create-physical-card-service/', views.generate_physical_card_service, name='generate_physical_card_service'),
    path('create-electronic-card-sum/', views.generate_electronic_card_sum, name='generate_electronic_card_sum'),
    path('create-electronic-card-service/', views.generate_electronic_card_service, name='generate_electronic_card_service'),
    path('electronic-card-display-sum/', views.electronic_card_sum_display, name='electronic_card_sum_display'),
    path('electronic-card-records/', views.electronic_cards_records, name='electronic_cards_records'),
   
    path('physical-card-records-service/', views.physical_card_service_records, name='physical_card_service_records'),
    path('electronic-card-records-service/', views.electronic_card_service_records, name='electronic_card_service_records'),
    path('electronic-card-display-service/', views.electronic_card_service_display, name='electronic_card_service_display'),
    path('register-cards/', views.register_cards, name='register_cards'),
    path('deduct-electronic-sum/<int:pk>/', views.electronic_card_sum_deduct_amount, name='electronic_card_sum_deduct_amount'),
   
    path('deduct-physical-service/<int:pk>/', views.physical_card_service_deduct_amount, name='physical_card_service_deduct_amount'),
    path('deduct-electronic-service/<int:pk>/', views.electronic_card_service_deduct_amount, name='electronic_card_service_deduct_amount'),
    

]
