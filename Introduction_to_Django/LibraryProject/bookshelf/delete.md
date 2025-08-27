# Delete Operation

```python
from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>

