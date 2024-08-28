
# Rumi Press Book Distribution Web Application

## Overview
This project is a Django-based web application designed to automate and manage the book distribution process for Rumi Press, a leading book distribution house in the EdTech industry. The application allows for efficient management of book categories, book information, and distribution expenses.

## Features
- **CRUD Operations for Book Categories**: Create, read, update, and delete book categories.
- **CRUD Operations for Books**: Manage book details including title, author, publishing date, category, and distribution expenses.
- **Data Import**: Import existing book data from Excel spreadsheets.
- **Expense Reports**: Generate reports showing distribution expenses by book category.

## Project Structure

- **books/**: Contains the Django app for managing books and categories.
  - **migrations/**: Database migrations.
  - **templates/**: HTML templates for the app.
    - **books/**: Templates for CRUD operations and reports.
  - **admin.py**: Admin interface configuration.
  - **apps.py**: App configuration.
  - **forms.py**: Forms for creating and updating book categories and books.
  - **models.py**: Data models for book categories and books.
  - **urls.py**: URL routing for the app.
  - **views.py**: Views handling CRUD operations and reports.

## Setup and Installation

**Clone the Repository**
   '''bash
   git clone <repository_url>
   cd rumi_press
   
### Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate     # For Windows

### Install Dependencies
pip install -r requirements.txt

### Apply Migrations
python manage.py migrate

### Create a Super user
python manage.py createsuperuser

### Run the Development server
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to access the application.


### Importing Data
Place your Excel file in the data/ directory (e.g., data/books_data.xlsx).

Use the Django shell or create a management command to import the data:
python manage.py shell
'''
from books.utils import import_books_from_spreadsheet
import_books_from_spreadsheet()

### Templates
* category_list.html: Displays a list of book categories.
* category_form.html: Form for creating and editing book categories.
* book_list.html: Displays a list of books.
* book_form.html: Form for creating and editing books.
* expense_report.html: Shows distribution expenses by book category.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
