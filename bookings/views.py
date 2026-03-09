from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def index(request):
    # Home page view
    return render(request, 'bookings/index.html')


@login_required
def booking_list(request):
    # Show all bookings for the logged in user
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_create(request):
    # Create a new booking
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been created successfully!')
            return redirect('booking_list')
        else:
            messages.error(request, 'There was an error with your booking. Please check the form.')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form, 'action': 'Create'})


@login_required
def booking_edit(request, pk):
    # Edit an existing booking
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated successfully!')
            return redirect('booking_list')
        else:
            messages.error(request, 'There was an error updating your booking. Please check the form.')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form, 'action': 'Edit'})


@login_required
def booking_delete(request, pk):
    # Delete an existing booking
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been cancelled successfully!')
        return redirect('booking_list')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})


def register(request):
    # Register a new user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to The Grand Table!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error creating your account. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
