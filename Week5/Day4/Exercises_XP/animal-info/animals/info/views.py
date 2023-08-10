
from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families
# Create your views here.

def display_all_animals(request):
    list_animals = "<ul>Animals:"
    
    for animal in animals:
        list_animals += f'<li>Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}</li>'
    
    list_animals += "</ul>"
    return HttpResponse(list_animals)
    

def display_all_families(request):
    list_families = "<ul>Families:"
    for family in families:
        list_families += f'<li>Name: {family["name"]}</li>'
    list_families += "</ul>"   
    return HttpResponse(list_families)   
 
def display_one_animal(request, id:int):
    for animal in animals:
        if animal['id'] == id:
            one_animal = f'Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}'
    return HttpResponse(one_animal) 

def animal_in_family(request, f_id:int):
    animals_families = f'<ol>Animal in family {families[f_id-1].get("name")}:'
    for animal in animals:
        if animal['family'] == f_id:
            animals_families += f'<li>Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}</li>'
    animals_families += '</u>' 
    return HttpResponse(animals_families) 