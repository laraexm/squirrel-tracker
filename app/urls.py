from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
        path('sightings/', views.index),
        path('<int:squirrel_id>/', views.detail, name='detail'),
        path('map/', views.map),
        path('sightings/add/', views.create_new_sighting, name='Create New Sighting'),
        ]


