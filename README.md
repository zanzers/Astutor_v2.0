# Create Project Main  
django-admin startproject demo  

# Create App  
python manage.py startapp myApp  

# Link the project  
In the `settings.py` file inside the main project folder,  
go to `INSTALLED_APPS` and add your newly created app name.  

# Step in the new app  
Create `urls.py`  
In `views.py`, add your view functions  
Then link the new views in the newly created `urls.py` file  

```python
# myApp/urls.py
from django.urls import path  
from . import views  

urlpatterns = [  
    path("", views.Home, name="home")  
]
