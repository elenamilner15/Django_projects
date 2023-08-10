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
    person_info = (
                f"Name: {name}, Age: {age}, Country: {country}"                
            )
    return HttpResponse(person_info)


def display_people(request):
    people_info = '\n'.join(people)        
    return HttpResponse(people_info)


def display_all_people(request):
    sorted_people = sorted(all_people, key=lambda x: x['age'])
    
    all_people_info = []
    for item in sorted_people:        
        info = (
            f"Id: {item['id']}, Name: {item['name']}, Age: {item['age']}, Country: {item['country']}"
        )
        all_people_info.append(info) 
    all_people_info = '\n'.join(all_people_info)        
    return HttpResponse(all_people_info)

   
def index(response):
	return render(response, "info/index.html", {})