from django.contrib import admin
from .models import Microorganism, CultureMedia, MorphologicalClassification # import the Microorganism, CultureMedia and MorphologicalClassification models from models.py


# Register your models here.
admin.site.register(Microorganism) 
admin.site.register(CultureMedia)
admin.site.register(MorphologicalClassification)
# these lines will add the models to the admin panel
