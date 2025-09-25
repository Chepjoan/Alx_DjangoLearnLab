from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for the Book model.
# Converts Book objects into JSON and validates input data.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # include all fields from the Book model

    # Custom validation to make sure a book cannot be created
    # with a publication year in the future.
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model.
# Includes the author's name and a nested list of their related books.
# The nested relationship is handled by including the BookSerializer
# with many=True (since an author can have many books).
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
