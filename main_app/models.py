from django.db import models

# Create your models here.
class Microorganism(models.Model):
    name = models.CharField(max_length=400)
    img = models.CharField(max_length=600)
    characteristics = models.TextField(max_length=3000)
    description = models.TextField(max_length=3000)
    manifestation = models.TextField(max_length=3000)
    laboratory_diagnosis = models.TextField(max_length=3000)
    verified_microorganism = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Microorganism: " + self.name

    class Meta:
        ordering = ['name'] 


class CultureMedia(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    microorganism = models.ForeignKey(Microorganism, on_delete=models.CASCADE, related_name="culture_medias")

    def __str__(self):
        return self.name

class MorphologicalClassification(models.Model):

    name = models.CharField(max_length=300)
    # this is going to create the many to many relationship and join table
    culture_medias = models.ManyToManyField(CultureMedia)

    def __str__(self):
        return self.name
