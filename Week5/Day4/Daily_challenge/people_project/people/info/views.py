from django.shortcuts import render
from django.http import HttpResponse

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
    person = f'{name} {age} y.o. from {country}'
    return HttpResponse(person)

def display_people(request):
    capitalize_people = '<ul>'
    for person in people:
        capitalize_people += f'<li>{person.capitalize()}</li>'
    capitalize_people += '</ul>'
    return HttpResponse(capitalize_people) 

def display_all_people(request):
    allpeople = '<ol>'
    for person in all_people:
        allpeople += f'<li>{person["name"]} {person["age"]} y.o. from {person["country"]}</li>'
    allpeople += '</ol>'
    return HttpResponse(allpeople)            