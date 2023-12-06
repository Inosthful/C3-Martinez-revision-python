from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'carApp/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    return render(request, 'carApp/car_detail.html', {'car': car})

def car_ratings(request):
    cars = Car.objects.all()
    return render(request, 'carApp/car_ratings.html', {'cars': cars})