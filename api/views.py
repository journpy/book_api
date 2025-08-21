from rest_framework import generics     # refactored

from books.models import Book
from .serializers import BookListSerializer, BookSerializer


class BookListView(generics.ListAPIView):
    """Book List API View."""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookDetailView(generics.RetrieveAPIView):
    """Detail view for a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookCreateView(generics.CreateAPIView):
    """View for creating a book object."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.RetrieveUpdateAPIView):
    """View to update a book instance."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookDeleteView(generics.RetrieveDestroyAPIView):
    """View to delete a Book object."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

     
