from django.urls import path
from .views import (
    BookListCreateView, 
    BookDetailUpdateDeleteView, 
    #BookCreateView, 
    #BookUpdateView,
    #BookDeleteView,
    UsersListCreateView,
    UserDetailUpdateDeleteView,
    StaffView,
)


urlpatterns = [
    # endpoints for book api
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailUpdateDeleteView.as_view(), name='book-detail'),
    #path('create/', BookCreateView.as_view(), name='book-create'),
    #path('books/<int:id>/update/', BookUpdateView.as_view(), name='book-update'),
    #path('books/<pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # endpoints for users api
    path('users/', UsersListCreateView.as_view(), name='users'),
    path('users/<int:id>/', UserDetailUpdateDeleteView.as_view(), name='user-detail'),
    path('staff/', StaffView.as_view(), name='staff'),

]
