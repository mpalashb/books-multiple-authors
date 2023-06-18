from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return f"{self.name}"

class BookManager(models.Manager):
    def get_books_with_authors(self, author_names):
        authors_names_by_queryList = Author.objects.values_list('name', flat=True)
        check_only_list = [name for name in authors_names_by_queryList if name not in author_names]

        queryset = self.get_queryset()
        queryset = queryset.filter(authors__name__in=author_names)
        queryset = queryset.exclude(authors__name__in=check_only_list)
        return queryset.distinct() # distinct for without duplicates

class Book(models.Model):
    authors = models.ManyToManyField('Author', related_name='books')
    title = models.CharField(max_length=225)
    desc = models.TextField(blank=True, null=True)

    objects = BookManager()

    def __str__(self) -> str:
        return f"{self.title}"
    
