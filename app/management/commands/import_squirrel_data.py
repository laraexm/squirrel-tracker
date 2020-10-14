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
            
            for item in reader:
                obj = Squirrel()
                obj.X_Latitude = item['X_Latitude']
                obj.Y_Longitude = item['Y_Longitude']
                obj.Unique_Squirrel_ID = item['Unique_Squirrel_ID']
                obj.Shift = item['Shift']
                obj.Date = item['Date']
                obj.age = item['age']
                obj.Primary_Fur_Color = item['Primary_Fur_Color']
                obj.Location = item['Location']
                obj.Specific_Location = item['Specific_Location']
                obj.Running = item['Running']
                obj.Chasing = item['Chasing']
                obj.Climbing = item['Climbing']
                obj.Eating = item['Eating']
                obj.Foraging = item['Foraging']
                obj.Other_Activity = item['Other_Activity']
                obj.Kuks = item['Kuks']
                obj.Quaas = item['Quaas']
                obj.Moans = item['Moans']
                obj.Tail_Flags = item['Tail_Flags']
                obj.Tail_Twitches = item['Tail_Twitches']
                obj.Approaches = item['Approaches']
                obj.Indifferent = item['Indifferent']
                obj.Runs_From = item['Runs_From']

                obj.save()

        msg = f'you are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))


