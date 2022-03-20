from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=20, null=True)
    name_book = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.name_book
