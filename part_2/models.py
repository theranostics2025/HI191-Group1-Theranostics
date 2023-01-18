from django.db import models
from part_1.models import *

# class Equipment(models.Model):
#     name = models.CharField(max_length=300,null=True)
#     slug = models.SlugField(null=True)
    
#     def __str__(self):
#         return self.name

#CLASS THERAPY ONLY SUPPORTS ONE ENTRY PER PATIENT AS OF NOW. OPTIMIZE LATER    
class Therapy(models.Model):
    #patient_code = foreignkeyofpatientcode
    #age = foreignkeyofpatientcode
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )
    date_of_psma = models.DateField()
    premedications = models.CharField(max_length=120, null=True, blank=True)
    medications = models.CharField(max_length=120, null=True, blank=True)
    furosemide = models.BooleanField()
    systolic = models.IntegerField(blank=True, null=True)
    diastolic = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    rr = models.IntegerField(blank=True, null=True)
    saturation = models.IntegerField(blank=True, null=True)
    date_therapy = models.DateField()
    radiopharm = models.CharField(max_length=120, null=True, blank=True)
    side_effects = models.CharField(max_length=120, choices = SIDE_EFFECTS)


