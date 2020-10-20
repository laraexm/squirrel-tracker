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
            
            Unique_ID_List = []
            for item in reader:
                if item['Unique Squirrel ID'] not in Unique_ID_List:
                    Unique_ID_List.append(item['Unique Squirrel ID'])
                    obj = Squirrel()
                    obj.X_Latitude = item['X']
                    obj.Y_Longitude = item['Y']
                    obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                    obj.Shift = item['Shift']
                    raw = item['Date']
                    date_str = raw[-4:]+'-'+ raw[:2]+'-'+raw[2:4]
                    date = datetime.datetime.strptime(date_str, '%Y-%m-%d') 
                    obj.Date = date
                    obj.Age = item['Age']
                    obj.Primary_Fur_Color = item['Primary Fur Color']
                    obj.Location = item['Location']
                    obj.Specific_Location = item['Specific Location']
                    obj.Running = str(item['Running']) == 'TRUE'
                    obj.Chasing = str(item['Chasing']) == 'TRUE'
                    obj.Climbing = str(item['Climbing']) == 'TRUE'
                    obj.Eating = str(item['Eating']) == 'TRUE'
                    obj.Foraging = str(item['Foraging']) == 'TRUE'
                    obj.Other_Activity = str(item['Other Activities']) == 'TRUE'
                    obj.Kuks = str(item['Kuks']) == 'TRUE'
                    obj.Quaas = str(item['Quaas']) == 'TRUE'
                    obj.Moans = str(item['Moans']) == 'TRUE'
                    obj.Tail_Flags = str(item['Tail flags']) == 'TRUE'
                    obj.Tail_Twitches = str(item['Tail twitches']) == 'TRUE'
                    obj.Approaches = str(item['Approaches']) == 'TRUE'
                    obj.Indifferent = str(item['Indifferent']) == 'TRUE'
                    obj.Runs_From = str(item['Runs from']) == 'TRUE'

                    obj.save()
                else:
                    pass

        msg = f'you are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))


