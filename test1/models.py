from django.db import models

# Create your models here.


class Student(models.Model):
    nom=models.CharField(max_length=255)
    email=models.CharField(max_length=15, unique=True)

    
