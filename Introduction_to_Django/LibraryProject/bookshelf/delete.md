
---

### 4️⃣ `delete.md`
```markdown
# Delete the Book instance

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
