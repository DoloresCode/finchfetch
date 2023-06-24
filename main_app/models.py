from django.db import models

# Create your models here.
class Microorganism(models.Model):
    name = models.CharField(max_length=400)
    img = models.CharField(max_length=600)
    characteristics = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    manifestation = models.TextField(max_length=1000)
    laboratory_diagnosis = models.TextField(max_length=1000)
    verified_microorganism = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Microorganism: " + self.name

    class Meta:
        ordering = ['name'] 


