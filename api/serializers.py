from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)


class BookSerializer(serializers.ModelSerializer):  # refactored
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',
            )
