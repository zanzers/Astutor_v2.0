# Create Project Main 
django-admin startproject demo

# Create App 
py manage.py startapp myApp

# link the project 
in the setting.py main folder
under of ISNTALLED_APPS add your 
newly add app name

# Step in the New app

create urls.py
In views.py add functions
add the new views in the newly urls.py

# from django.urls import path
# from . import views 
# urlpatterns = [
#     path("", views.Home, name="home")
# ]

proced on the urls.py under of the main project 
and add the urlpatterns of the new app.

# py manage.py runserver

add folder in the app name
templates inside of this folder
add html files.