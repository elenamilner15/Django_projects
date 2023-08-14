from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_books/', views.list_books, name='list_books'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('create_book/', views.create_book, name='create_book'),
]
