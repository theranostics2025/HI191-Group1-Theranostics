from django.db import models
from part_1.models import Patient

# Create your models here.
class PostTherapy(models.Model):
    LESIONS = (
        ('Prostate', 'Prostate'),
        ('Lymph Nodes', 'Lymph Nodes'),
        ('Bones', 'Bones'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver')
    )
    #count = id ng 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_post_therapy = models.DateField()
    post_therapy_scan_hours = models.IntegerField(blank=True, null=True)
    with_spect_ct = models.BooleanField()
    lesions = models.CharField(max_length=120, choices = LESIONS) #MAKE SURE MULTIPLE CHOICE FIELD FOR FORMS
    bone_lesion_details = models.TextField(blank=True, null=True)
    lesion_image = models.ImageField(blank=True)
    

    #Dosimetry
    salivary_gland = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kidney_left = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kidney_right = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dosimetry_image = models.ImageField(blank=True)
    