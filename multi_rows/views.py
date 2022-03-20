from django.forms import formset_factory
from django.shortcuts import render, redirect

from multi_rows.forms import BookForm
from multi_rows.models import Book


def book_view(request):
    if request.method == 'POST':
        Order = formset_factory(BookForm, extra=3)
        formset = Order(request.POST)
        if formset.is_valid():
            for form in formset:
                book_name = form.cleaned_data.get('name_book')
                author = form.cleaned_data.get('author')
                if book_name:
                    Book(name_book=book_name, author=author).save()
            return redirect(book_view)
    else:
        Order = formset_factory(BookForm, extra=3)
        formset = Order()
        return render(request, 'multi_rows/Book.htm', {'formset': formset})
