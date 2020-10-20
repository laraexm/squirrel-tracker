from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
        path('map/', views.map),
        path('sightings/', views.index,name='index'),
        path('sightings/stats/', views.stats, name='stats'),
        path('sightings/add/', views.create_new_sighting, name='Create New Sighting'),
        path('sightings/<Unique_Squirrel_ID>/', views.update_sighting, name='Update Sighting'),
        ]


