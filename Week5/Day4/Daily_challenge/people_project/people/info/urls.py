from django.urls import path
from .views import display_person, display_people, display_all_people

urlpatterns = [
    path('person/', display_person, name='person'),
    path('people/', display_people, name='people'),
    path('all_people/', display_all_people, name='all_people'),
]