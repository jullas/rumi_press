from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import BookCategory
from .forms import BookCategoryForm
from .models import Book
from .forms import BookForm
from django.db.models import Sum


def category_list(request):
    categories = BookCategory.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = BookCategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = BookCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = BookCategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = BookCategory.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

# Similarly, implement update and delete views for books


def expense_report(request):
    report = Book.objects.values('category__name').annotate(total_expenses=Sum('distribution_expenses'))
    return render(request, 'expense_report.html', {'report': report})


