from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=20)
    text=models.CharField(max_length=50)
    date=models.DateField()
    datee=models.DateField()