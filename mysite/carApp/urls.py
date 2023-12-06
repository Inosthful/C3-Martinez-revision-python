from django.urls import path
from .views import car_list, car_detail, car_ratings

urlpatterns = [
    path('', car_list, name='car_list'),  # URL racine de l'application
    path('<int:car_id>/', car_detail, name='car_detail'),
    path('ratings/', car_ratings, name='car_ratings'),

]