# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/', views.make_reservation, name='make_reservation'),
    # Add more URLs as needed
]