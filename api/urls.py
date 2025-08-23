from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView,
    BookDeleteView,
    UsersListView,
    UserDetailView,
    StaffView,
)


urlpatterns = [
    # endpoints for book api
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:id>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # endpoints for users api
    path('users/', UsersListView.as_view(), name='users'),
    path('users/<pk>/', UserDetailView.as_view(), name='user-detail'),
    path('staff/', StaffView.as_view(), name='staff'),

]
