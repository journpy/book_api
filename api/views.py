from rest_framework.generics import ListAPIView, RetrieveAPIView

from books.models import Book
from .serializers import BookListSerializer, BookDetailSerializer


class BookListView(ListAPIView):
    """Book List API View."""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookDetailView(RetrieveAPIView):
    """Detail view for a book."""
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = 'id'

     
