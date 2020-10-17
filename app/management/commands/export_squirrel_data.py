
from django.http import HttpResponse

import csv

from django.core.management.base import BaseCommand

from app.models import Squirrel


class Command(BaseCommand):
    help = 'export the squirrel data csv'

    def add_arguments(self,parser):
        parser.add_argument('file', help='file to be exported')

    def handle(self, *args, **options):
        file_=options['file']
        squirrels = Squirrel.objects.all()
        with open(file_, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['X_Latitude','Y_Longitude','Unique_Squirrel_ID','Shift','Date','Age',
                'Primary_Fur_Color','Location','Running','Chasing','Climbing','Eating','Foraging',
                'Other_Activity','Kuks','Quaas','Moans','Tail_Flags','Tail_Twitches','Approaches',
                'Indifferent','Runs_From'])
            for obj in squirrels:
                writer.writerow([obj.X_Latitude,obj.Y_Longitude,obj.Unique_Squirrel_ID,obj.Shift,obj.Date,obj.Age,
                obj.Primary_Fur_Color, obj.Location,obj.Running,obj.Chasing,obj.Climbing,obj.Eating,obj.Foraging,
                obj.Other_Activity,obj.Kuks,obj.Quaas,obj.Moans,obj.Tail_Flags, obj.Tail_Twitches,obj.Approaches,
                obj.Indifferent,obj.Runs_From])
        csvfile.close()
        print (f'Data written scccessufully!')
