# bookings/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'bookings/home.html')

def make_reservation(request):
    return render(request, 'bookings/make_reservation.html')
    # Implement the logic to handle form submission and database operations