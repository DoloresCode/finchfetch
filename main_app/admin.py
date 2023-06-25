from django.contrib import admin
from .models import Microorganism, CultureMedia # import the Microorganism and CultureMedia models from models.py


# Register your models here.
admin.site.register(Microorganism) 
admin.site.register(CultureMedia)
# these lines will add the models to the admin panel
