from django.urls import path
from .views import (
    AuthorListCreateView,
    BookListCreateView, 
    BookDetailUpdateDeleteView, 
    UsersListCreateView,
    UserDetailUpdateDeleteView,
    StaffView,
)


urlpatterns = [
    # endpoints for book api
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailUpdateDeleteView.as_view(), name='book-detail'),
    path('authors/', AuthorListCreateView.as_view(), name='authors'),
    # endpoints for users api
    path('users/', UsersListCreateView.as_view(), name='users'),
    path('users/<int:id>/', UserDetailUpdateDeleteView.as_view(), name='user-detail'),
    path('staff/', StaffView.as_view(), name='staff'),

]
