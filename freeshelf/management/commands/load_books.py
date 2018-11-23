from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from freeshelf.models import Book


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'freeshelf', file)


class Command(BaseCommand):
    help = "Load books from booklist.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting books...")
        Book.objects.all().delete()
        with open(get_path('booklist.csv'), 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(
                    name=row['name'],
                    author=row['author'],
                    description=row['description'],
                    date_added=row['date'],
                    category=row['category']
                )
                book.save()
