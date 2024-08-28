import os
import pandas as pd
from .models import Book, BookCategory

def import_books_from_spreadsheet():
    file_path = os.path.join('data', 'Books.xlsx')
    data = pd.read_excel(file_path)
    for _, row in data.iterrows():
        category, created = BookCategory.objects.get_or_create(name=row['Category'])
        Book.objects.create(
            title=row['Title'],
            author=row['Author'],
            publishing_date=row['Publishing Date'],
            category=category,
            distribution_expenses=row['Distribution Expenses']
        )