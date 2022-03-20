from django import forms

from multi_rows.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'name_book')
