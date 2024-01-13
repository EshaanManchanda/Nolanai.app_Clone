from django.db import models

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

GENRE_CHOICES = (
        ('sci-fi', 'Science Fiction'),
        ('horror', 'Horror'),
        ('fantasy', 'Fantasy'),
        ('romance', 'Romance'),
        # Add more genres as needed
    )


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    scripts = models.ManyToManyField('Scripts',default="NULL")   

class Scripts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Plot= models.CharField(max_length=500,default="NULL")
    scenes = models.JSONField()
    characters = models.JSONField()
    pdf_format = models.FileField(upload_to='scripts/')

    
# Create your models here.

