# Update Operation

```python
from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Check the updated book
book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>


