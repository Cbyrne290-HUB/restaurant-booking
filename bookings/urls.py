from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_create, name='booking_create'),
    path('bookings/<int:pk>/edit/', views.booking_edit, name='booking_edit'),
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
    path('register/', views.register, name='register'),
]
