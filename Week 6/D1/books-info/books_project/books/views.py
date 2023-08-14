from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json
import requests


def list_books(request):
    books = Book.objects.all()
    data = [{'title': book.title, 'author': book.author,
             'published_date': book.published_date} for book in books]
    return JsonResponse(data, safe=False)


def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        data = {'title': book.title, 'author': book.author, 'published_date': book.published_date, 'description': book.description,
                'page_count': book.page_count, 'categories': book.categories, 'thumbnail_url': book.thumbnail_url}
        return JsonResponse(data)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)


@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        author = data.get('author')
        published_date = data.get('published_date')
        description = data.get('description')
        page_count = data.get('page_count')
        categories = data.get('categories')
        thumbnail_url = data.get('thumbnail_url')

        book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            description=description,
            page_count=page_count,
            categories=categories,
            thumbnail_url=thumbnail_url
        )
        response_data = {
            'message': 'Book created successfully',
            'book_id': book.id,
            'title': book.title
        }
        return JsonResponse(response_data, status=201)

    else:
        return JsonResponse({'error': 'Invalid request method'})


def import_books():
    search_terms = 'python'
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q={search_terms}')
    data = response.json()

    for item in data.get('items', []):
        volume_info = item.get('volumeInfo')
        title = volume_info.get('title')
        authors = volume_info.get('authors', [])
        author = ", ".join(authors)
        published_date = volume_info.get('publishedDate')
        description = volume_info.get('description', '')
        page_count = volume_info.get('pageCount', 0)
        categories = ', '.join(volume_info.get('categories', []))
        thumbnail_url = volume_info.get('imageLinks', {}).get('thumbnail', '')

        try:
            book = Book.objects.get(title=title)
        except Book.DoesNotExist:
            book = Book.objects.create(
                title=title,
                author=author,
                published_date=published_date,
                description=description,
                page_count=page_count,
                categories=categories,
                thumbnail_url=thumbnail_url
            )
            print(f"Created book: {book.title}")
        else:
            print(f"Book already exists: {book.title}")


def index(request):
    return HttpResponse("Welcome to the Books App")
