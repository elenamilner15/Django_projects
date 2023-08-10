from django.shortcuts import render
from django.http import HttpResponse
from info.data import animals, families

def index(request):
    return HttpResponse("Hello, world. You're at the animals-info")

def display_all_animals(request):  
    all_animals = []
    for animal in animals:
        all_animals.append(
            f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, "
            f"Height: {animal['height']}, Speed: {animal['speed']}"
        )    
    all_animals = '\n'.join(all_animals)
    return HttpResponse(all_animals)


def display_all_families(request):  
    all_families = []
    for family in families:
        all_families.append(
            f"Name: {family ['name']}"
        )   
    all_families = '\n'.join(all_families)
    return HttpResponse(all_families)

def display_one_animal(request, animal_id):  
    one_animal = []
    for animal in animals:     
        if animal['id'] == animal_id:                 
            one_animal = (
            f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, "
            f"Height: {animal['height']}, Speed: {animal['speed']}"
        )        
        return HttpResponse(one_animal)
    else:        
        return HttpResponse("Animal not found")
            
            
def animal_per_family(request, family_id):  
    family_animals_info = []
    for animal in animals:
        if animal['family'] == family_id:
            animal_info = (
                f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, "
                f"Height: {animal['height']}, Speed: {animal['speed']}"
            )
            family_animals_info.append(animal_info)
    
    if family_animals_info:
        response_content = '\n'.join(family_animals_info)
        return HttpResponse(response_content)
    else:
        return HttpResponse("No animals found for the given family ID.")
    
       
       
def index(response):
	return render(response, "info/index.html", {})