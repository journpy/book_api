from rest_framework import generics, permissions     # refactored
from django.contrib.auth.models import User
from books.models import Book
from .serializers import BookSerializer, UserSerializer



class BookListCreateView(generics.ListCreateAPIView):
    """Book List Create API View."""
    permission_classes = [permissions.AllowAny,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    page_size = 3


class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """View, update or delete for a book."""
    permission_classes = [permissions.AllowAny,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class UsersListCreateView(generics.ListCreateAPIView):
    """List and Create users"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    page_size = 3


class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """View, edit, or delete a user."""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class StaffView(generics.ListAPIView):
    """All staff"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer

     
