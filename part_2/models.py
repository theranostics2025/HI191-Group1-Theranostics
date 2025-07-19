from django.db import models
from part_1.models import *
from multiselectfield import MultiSelectField

# class Equipment(models.Model):
#     name = models.CharField(max_length=300,null=True)
#     slug = models.SlugField(null=True)
    
#     def __str__(self):
#         return self.name

#CLASS THERAPY ONLY SUPPORTS ONE ENTRY PER PATIENT AS OF NOW. OPTIMIZE LATER    

class Therapy(models.Model):
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='t_patient')
    date_of_psma = models.DateField()
    premedications = models.CharField(max_length=120, null=True, blank=True)
    medications = models.CharField(max_length=120, null=True, blank=True)
    furosemide = models.BooleanField()
    systolic = models.PositiveIntegerField(blank=True, null=True) # accept only positive integers only
    diastolic = models.PositiveIntegerField(blank=True, null=True) # accept only positive integers only
    hr = models.PositiveIntegerField(blank=True, null=True) # accept only positive integers only
    rr = models.PositiveIntegerField(blank=True, null=True) # accept only positive integers only
    # saturation = models.PositiveIntegerField(blank=True, null=True) # accept only positive integers only
    saturation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date_therapy = models.DateField()
    radiopharm = models.CharField(max_length=120, null=True, blank=True)
    side_effects = MultiSelectField(max_length=120, choices = SIDE_EFFECTS)


