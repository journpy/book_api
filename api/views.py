from rest_framework import generics, permissions     # refactored
from django.contrib.auth.models import User
from books.models import Book
from .serializers import BookListSerializer, BookSerializer, UserSerializer



class BookListView(generics.ListAPIView):
    """Book List API View."""
    permission_classes = [permissions.AllowAny,]
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    page_size = 3


class BookDetailView(generics.RetrieveAPIView):
    """Detail view for a book."""
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookCreateView(generics.CreateAPIView):
    """View for creating a book object."""
    permission_classes = [permissions.IsAdminUser,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.RetrieveUpdateAPIView):
    """View to update a book instance."""
    permission_classes = [permissions.IsAdminUser,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookDeleteView(generics.RetrieveDestroyAPIView):
    """View to delete a Book object."""
    permission_classes = [permissions.IsAdminUser,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UsersListView(generics.ListAPIView):
    """List of users"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    page_size = 3


class UserDetailView(generics.RetrieveAPIView):
    """Details of a user."""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StaffView(generics.ListAPIView):
    """All staff"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer

     
