Group name: [Xiaomeng E & Shukun Wang]
UNIs: [sw3506, xe2000]
"UNIs: [sw3506, xe2000]"

# Squirrel Tracker: 
## A web-app used to keep track of the squirrels in central park

This is for the group project of IEORE4501 Tools for Analytics
for the semester of FallA 2020

Group Members:
* Xiaomeng E (laraexm)
* Shukun Wang (chilly-wang)

# Introduction
## Features
### /sightings/
    * This is the main page of the squirrel-tracker web app
    * About: general information about the web app
    * Link to Stats: Click to view some statistics of the existing sightings
    * Link to Map: Click to view a map of NYC with 100 squirrel sightings plotted on it
    * Link to Create New Sighting: Click to add a new sighting to the database
    * List of sightings: lists all squirrel sightings. Click 'See Details and Update' to make changes to exisiting sightings
    
### /sightings/<Unique_Squirrel_ID>/
    * This page is used to view the details and update a squirrel sighting
    * After updating the values, click update to save changes

### /map/
    * This page is a map of NYC with 100 random squirrel sightings plotted on it
    * Feel free to zoom in and zoom out
    
### /sightings/stats/
    * This page demonstrates some stats of the sightings data in the database
   
### /sightings/add/
    * This page is used to create a new squirrel sighting
   
# Technologies
   * This project utilizes Google VM as the main development instance
   * Django and Python 3 is used to create the website

# Launch
   * Step 1: Clone this repository to your machine and create directory '/squirrel-tracker/project/'
   
   * Step 2: Make sure you have installed pip and other relevant gadgets. Activate environment using command "source ../env/bin/activate" and "pip install -r requirements.txt"
   
   * Step 3: You can import data to the database using "python manage.py import_squirrel_data /path/to/file.csv", make sure the csv file is already on your machine
   
   * Step 4: To run on External IP, use "sudo /username/squirrel-tracker/env/bin/python manage.py runserver 0.0.0.0:80"
   
   * Step 5: Open browser to "http://ExternalIP:80/sightings/" to get to the main page, you are all set to use it!
   
   * Step 6: After using the website to add/update sightings, you can download a csv of the data to your machine by "python manage.py export_squirrel_data /path/to/file.csv"
