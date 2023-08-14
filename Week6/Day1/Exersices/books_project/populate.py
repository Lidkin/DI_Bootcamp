import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')
import django
django.setup()

from datetime import datetime
from books.models import Book
import requests

response = requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
data = response.json()

for item in data['items']:
    book_data = item['volumeInfo']
    published_date_str = book_data.get('publishedDate', None)

    # Convert the published date to a datetime object
    published_date = None
    if published_date_str:
        try:
            # If the date is in the yyyy/mm/dd format
            published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()
        except ValueError:
            try:
                # If the date is in the yyyy format
                published_date = datetime.strptime(published_date_str, '%Y').date()
            except ValueError:
                print("Could not parse date:", published_date_str)

    Book.objects.create(
        title=book_data['title'],
        author=', '.join(book_data['authors']),
        published_date=published_date,
        description=book_data.get('description', ''),
        page_count=book_data.get('pageCount', 0),
        categories=', '.join(book_data.get('categories', [])),
        thumbnail_url=book_data['imageLinks']['thumbnail'] if 'imageLinks' in book_data else ''
    )