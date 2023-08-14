from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json
# Create your views he.:

def list_books(request):
    books = Book.objects.all()
    book_data = [{'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date} for book in books]
    return JsonResponse({'books': book_data})

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        book_data = {'title': book.title, 'author': book.author, 'published_date': book.published_date, 'description': book.description, 'categories': book.categories}
        return JsonResponse({'book': book_data})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        book_data = json.loads(request.body)
        try:
            if not book_data['title'] and not book_data['authors'] and not book_data['publishedDate'] and not book_data['description'] and not book_data['categories']:
                raise Exception
            book = Book.objects.create(
                title=book_data['title'],
                author=', '.join(book_data['authors']),
                published_date=book_data.get('publishedDate'),
                description=book_data.get('description', ''),
                page_count=book_data.get('pageCount', 0),
                categories=', '.join(book_data.get('categories', [])),
                thumbnail_url=book_data['imageLinks']['thumbnail'] if 'imageLinks' in book_data else '')
            return JsonResponse({'book': book_data})
        except Exception:
           return JsonResponse({'error': book_data}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)