from django.db import models

class Patient(models.Model):
    age = models.IntegerField()