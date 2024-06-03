from django.urls import path
from .views import BookListView, BooksView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/get/<int:pk>/', BooksView.as_view(), name='book-details'),
    path('book/create/', BooksView.as_view(), name='book-create'),
    path('book/update/<int:pk/', BooksView.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', BooksView.as_view(), name='book-delete')
] 