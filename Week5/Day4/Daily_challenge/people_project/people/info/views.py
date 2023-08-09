from django.shortcuts import render
from django.http import HttpResponse
from operator import itemgetter


# Create your views here.
name = 'Bob Smith'
age = 35
country = 'USA'

people = ['bob','martha', 'fabio', 'john']

all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def display_person(request):
    person = f'{name} {age} yo from {country}'
    return HttpResponse(person)

def display_people(request):
    cap_people = [x.capitalize() for x in sorted(people)]
    return HttpResponse(', '.join(cap_people))

def display_all_people(request):
    list_all_people = [ f'{person["name"]} {person["age"]} yo from {person["country"]}' for person in sorted(all_people, key=itemgetter('age'))]
    all_p = ' || '.join(list_all_people)
    return HttpResponse(all_p)