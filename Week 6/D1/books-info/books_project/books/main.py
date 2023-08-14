import requests
from django.core.exceptions import ObjectDoesNotExist
from .models import Book


def import_books():
    search_terms = 'python'
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q={search_terms}')
    data = response.json()

    for item in data.get('items'):
        volume_info = item.get('volumeInfo')
        title = volume_info.get('title')
        author = volume_info.get('authors')[
            0] if 'authors' in volume_info else ''
        published_date = volume_info.get('publishedDate', None)
        description = volume_info.get('description', '')
        page_count = volume_info.get('pageCount', 0)
        categories = ', '.join(volume_info.get('categories', []))
        thumbnail_url = volume_info.get('imageLinks', {}).get('thumbnail', '')

        try:
            book = Book.objects.get(title=title)
        except ObjectDoesNotExist:
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
