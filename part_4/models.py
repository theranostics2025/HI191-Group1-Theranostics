from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from datetime import datetime

class Patient(models.Model):
    TYPE_TREATMENT = (
        ('Hormonal Treatment', 'Hormonal Treatment'),
        ('Radiation Therapy', 'Radiation Therapy'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Others', 'Others'),
    )
    
    name = models.CharField(max_length=120, blank= False, null=True)
    slug = models.SlugField(null=True)
    age = models.IntegerField(validators=[MinValueValidator(0, message="Age cannot be negative")])
    address = models.CharField(max_length=300)
    diagnosis_date = models.DateField()
    surgery_date = models.DateField()
    histopath_result = models.ImageField(upload_to="images/")
    histopath_details = models.TextField(max_length=200, blank=False, null=True)
    
    GLEASON_CHOICES = [
        ('', '----------'),
        ('<6', 'Less than 6'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    ]
    
    gleason_score = models.CharField(
        max_length=2,
        choices=GLEASON_CHOICES,
        default='',
        blank=True,
        null=True
    )
    
    date_of_treatment = models.DateField()
    type_of_treatment = models.CharField(max_length=120, choices=TYPE_TREATMENT)

    def __str__(self): 
        return self.name

    #auto-add slugs
    def save(self, *args1, **args2):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args1, **args2)

class PhysicalExam(models.Model):
    ECOG_CHOICES = [
        (0, '0 - Fully active'),
        (1, '1 - Restricted but ambulatory'),
        (2, '2 - Ambulatory but unable to work'),
        (3, '3 - Limited self-care'),
        (4, '4 - Completely disabled'),
        (5, '5 - Dead')
    ]

    id = models.AutoField(primary_key=True)
    date_recorded = models.DateField(default=datetime.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    
    # ECOG with validation
    ecog_score = models.IntegerField(
        choices=ECOG_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    
    # Physical measurements with decimal precision
    height = models.FloatField(
        validators=[MinValueValidator(0)],
    )
    weight = models.FloatField(
        validators=[MinValueValidator(0)],
    )
    bmi = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True
    )
    
    # Vital signs
    bp = models.CharField(
        max_length=120,
    )
    hr = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    
    # Clinical assessment
    pain_score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    local_symptoms = models.CharField(max_length=300, blank=True)
    systemic_symptoms = models.CharField(max_length=300, blank=True)

    def save(self, *args1, **args2):
        # Auto-calculate BMI if height and weight are provided
        if self.height and self.weight:
            height_in_meters = self.height / 100
            self.bmi = round(self.weight / (height_in_meters ** 2), 2)
        super().save(*args1, **args2)

    def __str__(self):
        return f"Physical Exam for {self.patient} on {self.date_recorded}"


class Screening(models.Model):
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='screening_patient')
    psa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    creatinine = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    wbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hemoglobin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hematocrit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    platelet = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lactate_hydrogenase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alkaline_phosphatase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bilirubins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    SALIVARY_GLAND_STATUS = (
        ('Normal', 'Normal'),
        ('Left Obstruction', 'Left Obstruction'),
        ('Right Obstruction', 'Right Obstruction')
    )
    salivary_gland_status = models.CharField(max_length=120, choices = SALIVARY_GLAND_STATUS)
    salivary_gland_image = models.ImageField(upload_to="images/", null=True)

    BONE_METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    bone_metastasis_status = models.CharField(max_length=120, choices = BONE_METASTASIS_STATUS, blank=True, null=True)
    bone_scan_image = models.ImageField(upload_to="images/", null=True)
    renal_scintigraphy = models.ImageField(upload_to="images/")

    GAPSMA = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    gapsma_choices = models.CharField(max_length=120, choices=GAPSMA, blank=True, null=True)
    gapsma_img = models.ImageField(upload_to="images/")

##THIS SEGMENT NEEDS OPTIMIZATION##
    # GAPSMA Lesions
    LESION_STATUS = (
        ('Absent', 'Absent'),
        ('Present', 'Present')
    )
    gapsma_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    gapsma_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_prostate_size = models.IntegerField(verbose_name="Prostate Lesion Size", blank=True, null=True)

    gapsma_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    gapsma_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_lymph_node_size = models.IntegerField(verbose_name="Lymph Node Lesion Size", blank=True, null=True)

    gapsma_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    gapsma_bone_suv = models.DecimalField(verbose_name="Bone SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_bone_size = models.IntegerField(verbose_name="Bone Lesion Size", blank=True, null=True)

    gapsma_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    gapsma_brain_suv = models.DecimalField(verbose_name="Brain SUV", blank=True, null=True)
    gapsma_brain_size = models.IntegerField(verbose_name="Brain Lesion Size", blank=True, null=True)

    gapsma_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    gapsma_lung_suv = models.DecimalField(verbose_name="Lung SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_lung_size = models.IntegerField(verbose_name="Lung Lesion Size", blank=True, null=True)

    gapsma_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    gapsma_liver_suv = models.DecimalField(verbose_name="Liver SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_liver_size = models.IntegerField(verbose_name="Liver Lesion Size", blank=True, null=True)

    fdgpetct_img = models.ImageField(upload_to="images/")

    # For fdgpetct

    fdgpetct_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    fdgpetct_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_prostate_size = models.IntegerField(verbose_name="Prostate Lesion Size", blank=True, null=True)

    fdgpetct_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    fdgpetct_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_lymph_node_size = models.IntegerField(verbose_name="Lymph Node Lesion Size", blank=True, null=True)

    fdgpetct_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_bone_suv = models.DecimalField(verbose_name="Bone SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_bone_size = models.IntegerField(verbose_name="Bone Lesion Size", blank=True, null=True)

    fdgpetct_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_brain_suv = models.DecimalField(verbose_name="Brain SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_brain_size = models.IntegerField(verbose_name="Brain Lesion Size", blank=True, null=True)

    fdgpetct_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_lung_suv = models.DecimalField(verbose_name="Lung SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_lung_size = models.IntegerField(verbose_name="Lung Lesion Size", blank=True, null=True)

    fdgpetct_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_liver_suv = models.DecimalField(verbose_name="Liver SUV", max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_liver_size = models.IntegerField(verbose_name="Liver Lesion Size", blank=True, null=True)

    assessment = models.CharField(max_length=120, choices=ASSESSMENT, blank=True, null=True)
    plan = models.TextField(max_length=120, blank=True, null=True)