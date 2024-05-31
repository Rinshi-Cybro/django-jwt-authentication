from django.urls import path
from .views import BooksListView


urlpatterns = [
    path('book/<int:pk>/', BooksListView.as_view(), name='book-detail'),
    path('books/', BooksListView.as_view(), name='books-list'),

] 