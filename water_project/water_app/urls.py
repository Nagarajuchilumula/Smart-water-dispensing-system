from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.create_order, name='create_order'),
    path('pay/<int:order_id>/', views.payment_page, name='payment'),
    path('success/<int:order_id>/', views.success_page, name='success'),

    # API for hardware
    path('api/check/<str:tap_id>/', views.check_order, name='check_order'),
    path('api/complete/<int:order_id>/', views.mark_dispensed, name='complete_order'),
    
    # API for payment status check
    path('api/check_payment/<int:order_id>/', views.check_payment_status, name='check_payment_status'),
]