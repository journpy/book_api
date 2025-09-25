from rest_framework import serializers
from books.models import Book, Author
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['prefix', 'name', 'books']


class BookSerializer(serializers.ModelSerializer):  
    author = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'isbn', 'author']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',
            )
