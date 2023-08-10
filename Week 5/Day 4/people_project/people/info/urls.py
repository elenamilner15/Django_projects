from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.index, name='index'),
    path("person/", views.display_person, name="person_info"), 
    path("people/", views.display_people, name="people_info"),  
    path("all_people/", views.display_all_people, name="all_people_info"), 
]
