# Django Admin Integration for Book Model

## Steps:
1. Registered the `Book` model in `bookshelf/admin.py`.
2. Created a custom `BookAdmin` class:
   - `list_display`: Shows title, author, and publication year in list view.
   - `list_filter`: Allows filtering books by author and publication year.
   - `search_fields`: Enables searching by title and author.
3. Created a superuser to access the admin.
4. Verified functionality by running the server and accessing `/admin`.

## Result:
The Book model is now fully manageable from the Django admin interface, with improved usability for filtering and searching book records.
