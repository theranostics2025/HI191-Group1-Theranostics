from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from part_1.models import Patient
from multiselectfield import MultiSelectField

# Create your models here.
class PostTherapy(models.Model):
    LESIONS = (
        ('Prostate', 'Prostate'),
        ('Lymph Nodes', 'Lymph Nodes'),
        ('Bones', 'Bones'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver')
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pt_patient')
    date_of_post_therapy = models.DateField()
    post_therapy_scan_hours = models.PositiveIntegerField() # accept only positive integers only
    with_spect_ct = models.BooleanField()
    lesions = MultiSelectField(max_length=120, choices = LESIONS) #MAKE SURE MULTIPLE CHOICE FIELD FOR FORMS
    bone_lesion_details = models.TextField()
    lesion_image = models.ImageField(upload_to="images/")#image

    #Dosimetry
    salivary_gland = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]) # accept positive real numbers only
    kidney_left = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]) # accept positive real numbers only
    kidney_right = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]) # accept positive real numbers only
    dosimetry_image = models.ImageField(upload_to="images/")
    
