from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# View to list and create Authors
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# View to list and create Books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.shortcuts import render

# Create your views here.
