from django.core.management.base import BaseCommand
from books.views import import_books


class Command(BaseCommand):
    help = 'Populate database with sample book data'

    def handle(self, *args, **options):
        import_books()
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated database with sample book data'))
