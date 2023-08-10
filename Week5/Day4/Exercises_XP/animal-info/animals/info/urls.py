from django.urls import path
from .views import display_all_animals, display_all_families, display_one_animal, animal_in_family

urlpatterns = [
    path('animals/', display_all_animals, name='animals'),
    path('families/', display_all_families, name='families'),
    path('animal/<int:animal_id>/', display_one_animal, name='/animal/X/'),
    path('animal_in_family/<int:f_id>/', animal_in_family, name='/animal_in_family/X/'),
]