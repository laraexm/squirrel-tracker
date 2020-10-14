import csv

from django.core.management.base import BaseCommand

from app.models import Squirrel

import datetime

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
                obj.X_Latitude = item['X']
                obj.Y_Longitude = item['Y']
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                obj.Shift = item['Shift']
                raw = item['Date']
                date_str = raw[-4:]+'-'+ raw[:2]+'-'+raw[2:4]
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d') 
                obj.Date = date
                obj.age = item['Age']
                obj.Primary_Fur_Color = item['Primary Fur Color']
                obj.Location = item['Location']
                obj.Specific_Location = item['Specific Location']
                obj.Running = item['Running']
                obj.Chasing = item['Chasing']
                obj.Climbing = item['Climbing']
                obj.Eating = item['Eating']
                obj.Foraging = item['Foraging']
                obj.Other_Activity = item['Other Activities']
                obj.Kuks = item['Kuks']
                obj.Quaas = item['Quaas']
                obj.Moans = item['Moans']
                obj.Tail_Flags = item['Tail flags']
                obj.Tail_Twitches = item['Tail twitches']
                obj.Approaches = item['Approaches']
                obj.Indifferent = item['Indifferent']
                obj.Runs_From = item['Runs from']

                obj.save()

        msg = f'you are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))


