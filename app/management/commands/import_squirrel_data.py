import csv

from django.core.management.base import BaseCommand

from app.models import Squirrel

class Command(BaseCommand):
    help = 'import the squirrel data csv'

    def add_arguments(self,parser):
        parser.add_argument('file', help='file containing squirrel details')

    def handle(self, *args, **options):
        file_=options['file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

        msg = f'you are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))


