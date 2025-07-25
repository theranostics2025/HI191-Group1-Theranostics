from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from part_1.models import Patient

class FollowUp(models.Model):
    date_of_follow_up = models.DateField()
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='fu_patient')
    psa = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    creatinine = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=1, blank=True, null=True)
    wbc = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    rbc = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    hemoglobin = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    hematocrit = models.DecimalField(validators=[MinValueValidator(0)], max_digits=5, decimal_places=2, blank=True, null=True)
    platelet = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    lactate_hydrogenase = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    alkaline_phosphatase = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    sgpt = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    sgot = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    bilirubins = models.DecimalField(validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    SALIVARY_GLAND_STATUS = (
        ('Normal', 'Normal'),
        ('Left Obstruction', 'Left Obstruction'),
        ('Right Obstruction', 'Right Obstruction')
    )
    salivary_gland_status = models.CharField(max_length=120, choices = SALIVARY_GLAND_STATUS)
    salivary_gland_image = models.ImageField(upload_to="images/")

    BONE_METASTASIS_STATUS = (
        ('With Metastasis', 'With Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    bone_metastasis_status = models.CharField(max_length=120, choices = BONE_METASTASIS_STATUS)
    bone_scan_image = models.ImageField(upload_to="images/")
    renal_scintigraphy = models.ImageField(upload_to="images/")

    GAPSMA = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    gapsma_choices = models.CharField(max_length=120, choices=GAPSMA)
    gapsma_img = models.ImageField(upload_to="images/")

##THIS SEGMENT NEEDS OPTIMIZATION##
    # GAPSMA Lesions
    LESION_STATUS = (
        ('Absent', 'Absent'),
        ('Present', 'Present')
    )
    gapsma_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    gapsma_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    gapsma_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    gapsma_prostate_size = models.DecimalField(verbose_name="Prostate Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    gapsma_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    gapsma_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    gapsma_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    gapsma_lymph_node_size = models.DecimalField(verbose_name="Lymph Node Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    gapsma_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    gapsma_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    gapsma_bone_suv = models.DecimalField(verbose_name="Bone SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    gapsma_bone_size = models.DecimalField(verbose_name="Bone Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    gapsma_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    gapsma_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    gapsma_brain_suv = models.DecimalField(verbose_name="Brain SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=3, blank=True, null=True)
    gapsma_brain_size = models.DecimalField(verbose_name="Brain Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    gapsma_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    gapsma_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    gapsma_lung_suv = models.DecimalField(verbose_name="Lung SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    gapsma_lung_size = models.DecimalField(verbose_name="Lung Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    gapsma_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    gapsma_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    gapsma_liver_suv = models.DecimalField(verbose_name="Liver SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    gapsma_liver_size = models.DecimalField(verbose_name="Liver Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    fdgpetct_img = models.ImageField(upload_to="images/")

    # For fdgpetct

    fdgpetct_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    fdgpetct_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    fdgpetct_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    fdgpetct_prostate_size = models.DecimalField(verbose_name="Prostate Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    fdgpetct_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    fdgpetct_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    fdgpetct_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    fdgpetct_lymph_node_size = models.DecimalField(verbose_name="Lymph Node Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    fdgpetct_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    fdgpetct_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_bone_suv = models.DecimalField(verbose_name="Bone SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    fdgpetct_bone_size = models.DecimalField(verbose_name="Bone Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    fdgpetct_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    fdgpetct_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_brain_suv = models.DecimalField(verbose_name="Brain SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=3, blank=True, null=True)
    fdgpetct_brain_size = models.DecimalField(verbose_name="Brain Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    fdgpetct_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    fdgpetct_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_lung_suv = models.DecimalField(verbose_name="Lung SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    fdgpetct_lung_size = models.DecimalField(verbose_name="Lung Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    fdgpetct_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, default='Absent')
    fdgpetct_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_liver_suv = models.DecimalField(verbose_name="Liver SUV", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)
    fdgpetct_liver_size = models.DecimalField(verbose_name="Liver Lesion Size", validators=[MinValueValidator(0)], max_digits=12, decimal_places=2, blank=True, null=True)

    assessment = models.CharField(max_length=120, choices=ASSESSMENT)
    plan = models.TextField(max_length=120)
    