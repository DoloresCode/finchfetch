from django.contrib import admin
from .models import Microorganism # import the Microorganism model from models.py


# Register your models here.
admin.site.register(Microorganism) # this line will add the model to the admin panel
