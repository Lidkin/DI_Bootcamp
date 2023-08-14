from django.urls import path
from .views import create_profile, delete_profile, list_profiles

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('delete_profile/<int:id>', delete_profile, name='delete_profile'),
    path('list', list_profiles, name='get_profiles')
]