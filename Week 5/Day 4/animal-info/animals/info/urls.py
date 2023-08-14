from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.index, name='index'),
    path("animals/", views.display_all_animals, name="animals"), 
    path("families/", views.display_all_families, name="families"), 
    path("animal/<int:animal_id>/", views.display_one_animal, name="one_animal"), 
    path("animal_in_family/<int:family_id>/", views.animal_per_family, name="animal_in_family"), 
]
