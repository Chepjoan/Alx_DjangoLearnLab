from django.db import models

# The Author model represents a writer who can have many books.
# Each author has only one required field: name.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# The Book model represents a single book written by an Author.
# Each book has a title, publication year, and a foreign key (author)
# that links it to one Author. This creates a one-to-many relationship:
# one Author -> many Books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # allows us to access books from an author object (author.books.all())
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
