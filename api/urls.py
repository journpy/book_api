from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView,
    BookDeleteView,
)


urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:id>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

]
