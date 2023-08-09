from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families
# Create your views here.

def display_all_animals(request):
    list_animals = []
    for animal in animals:
        list_animals.append(f'Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}')
    all_animals = ' || '.join(list_animals)
    return HttpResponse(all_animals)

def display_all_families(request):
    list_families = []
    for family in families:
        list_families.append(f'Name: {family["name"]}\t')
    all_families = ' || '.join(list_families)    
    return HttpResponse(all_families)   
 
def display_one_animal(request, id:int):
    for animal in animals:
        if animal['id'] == id:
            one_animal = f'Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}'
    return HttpResponse(one_animal) 

def animal_in_family(request, f_id:int):
    animals_families = []
    for animal in animals:
        if animal['family'] == f_id:
            animals_families.append(f'Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}, Family - {families[f_id-1].get("name")}')
    all_animals_by_family = ' || '.join(animals_families)
    return HttpResponse(all_animals_by_family) 