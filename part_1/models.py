from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class AutoIncrementField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

class SalivaryGland(models.Model):
    STATUS = (
        ('Normal', 'Normal'),
        ('Left Obstruction', 'Left Obstruction'),
        ('Right Obstruction', 'Right Obstruction')
    )
    status = models.CharField(max_length=120, choices = STATUS)
    sg_image = models.ImageField(blank=True)

class BoneScan(models.Model):
    METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    metastasis_status = models.CharField(max_length=120, choices = METASTASIS_STATUS)
    sg_image = models.ImageField()



class Gapsma(models.Model):
    CHOICES = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    choices = models.CharField(max_length=120, choices=CHOICES)
    gapsma_img = models.ImageField(blank=True)
    # lymph_node_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # bone_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # brain_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # lung_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # liver_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)

class Fdgpetct(models.Model):
    fdgpetct_img = models.ImageField(blank=True)
    # prostate_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # lymph_node_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # bone_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # brain_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # lung_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    # liver_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)



class Patient(models.Model):
    TYPE_TREATMENT = (
        ('Hormonal Treatment', 'Hormonal Treatment'),
        ('Radiation Therapy', 'Radiation Therapy'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Others', 'Others'),
    )
    #Test results and others are put to a different model
    name = models.CharField(max_length=120, blank= False, null=True)
    patient_code = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=300)
    diagnosis_date = models.DateField()
    surgery_date = models.DateField()
    histopath_result = models.ImageField(blank=True, null=True)
    gleason_score = models.IntegerField(blank=True, null=True)
    date_of_treatment = models.DateField()
    type_of_treatment = models.CharField(max_length=120, choices=TYPE_TREATMENT)
    ecog_score = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    bmi = models.IntegerField(blank=True, null=True) # Body Mass Index
    bp = models.IntegerField(blank=True, null=True) # Blood Pressure
    hr = models.IntegerField(blank=True, null=True) # Heart Rate
    pain_score = models.IntegerField(blank=True, null=True)
    local_symptoms = models.CharField(max_length=300, blank=True)
    systemic_symptoms = models.CharField(max_length=300, blank=True)
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    salivarygland = models.OneToOneField(SalivaryGland, on_delete=models.CASCADE, blank=True, null=True)
    METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    metastasis_status = models.CharField(max_length=120, choices = METASTASIS_STATUS, blank=True, null=True)
    sg_image = models.ImageField(blank=True, null=True)
    rs = models.ImageField(blank=True, null=True)
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
    assessment = models.CharField(max_length=120, choices=ASSESSMENT, blank=True, null=True)
    GAPSMA = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    choices = models.CharField(max_length=120, choices=GAPSMA, blank=True, null=True)
    gapsma_img = models.ImageField(blank=True, null=True)

##THIS SEGMENT NEEDS OPTIMIZATION##
    # GAPSMA Lesions
    LESION_STATUS = (
        ('Absent', 'Absent'),
        ('Present', 'Present')
    )
    gapsma_prostate_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_prostate_location = models.CharField(max_length=50, null=True, blank=True)
    gapsma_prostate_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_prostate_size = models.IntegerField(blank=True, null=True)

    gapsma_lymph_node_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lymph_node_location = models.CharField(max_length=50, null=True, blank=True)
    gapsma_lymph_node_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_lymph_node_size = models.IntegerField(blank=True, null=True)

    gapsma_bone_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_bone_location = models.CharField(max_length=50, null=True, blank=True)
    gapsma_bone_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_bone_size = models.IntegerField(blank=True, null=True)

    gapsma_brain_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_brain_location = models.CharField(max_length=50, null=True, blank=True)
    gapsma_brain_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_brain_size = models.IntegerField(blank=True, null=True)

    gapsma_lung_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lung_location = models.CharField(max_length=50, null=True, blank=True)
    gapsma_lung_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_lung_size = models.IntegerField(blank=True, null=True)

    gapsma_liver_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_liver_location = models.CharField(max_length=50, null=True, blank=True)
    gapsma_liver_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gapsma_liver_size = models.IntegerField(blank=True, null=True)

    fdgpetct_img = models.ImageField(blank=True)

    # For fdgpetct

    fdgpetct_prostate_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_prostate_location = models.CharField(max_length=50, null=True, blank=True)
    fdgpetct_prostate_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_prostate_size = models.IntegerField(blank=True, null=True)

    fdgpetct_lymph_node_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lymph_node_location = models.CharField(max_length=50, null=True, blank=True)
    fdgpetct_lymph_node_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_lymph_node_size = models.IntegerField(blank=True, null=True)

    fdgpetct_bone_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_bone_location = models.CharField(max_length=50, null=True, blank=True)
    fdgpetct_bone_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_bone_size = models.IntegerField(blank=True, null=True)

    fdgpetct_brain_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_brain_location = models.CharField(max_length=50, null=True, blank=True)
    fdgpetct_brain_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_brain_size = models.IntegerField(blank=True, null=True)

    fdgpetct_lung_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lung_location = models.CharField(max_length=50, null=True, blank=True)
    fdgpetct_lung_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_lung_size = models.IntegerField(blank=True, null=True)

    fdgpetct_liver_lesion_status = models.CharField(max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_liver_location = models.CharField(max_length=50, null=True, blank=True)
    fdgpetct_liver_suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fdgpetct_liver_size = models.IntegerField(blank=True, null=True)
    ##END OF SEGMENT##
    # prostate_lesion lymph_node_lesion bone_lesion brain_lesion lung_lesion liver_lesion

    def __str__(self): 
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.patient_code:
    #         qs = self.__class__.objects.filter(created__year=self.created.year)
    #         if qs.exists():
    #             self.patient_code = "{:04d}".format(qs.latest('created').patient_code + 1)
    #         else:
    #             self.patient_code = "{:04d}".format(1)
    #     super(Patient, self).save(*args, **kwargs)

# class PhysicalExam(models.Model):
#     patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
#     ecog_score = models.IntegerField(blank=True)
#     height = models.IntegerField(blank=True)
#     weight = models.IntegerField(blank=True)
#     bmi = models.IntegerField(blank=True) # Body Mass Index
#     bp = models.IntegerField(blank=True) # Blood Pressure
#     hr = models.IntegerField(blank=True) # Heart Rate
#     pain_score = models.IntegerField(blank=True)
#     local_symptoms = models.CharField(max_length=300, blank=True)
#     systemic_symptoms = models.CharField(max_length=300, blank=True)

# class Screening(models.Model):
#     ASSESSMENT = (
#         ('Low Risk', 'Low Risk'),
#         ('Intermediate Risk', 'Intermediate Risk'),
#         ('High Risk', 'High Risk'),
#     )
#     patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
#     salivarygland = models.OneToOneField(SalivaryGland, on_delete=models.CASCADE)
#     bonescan = models.OneToOneField(BoneScan, on_delete=models.CASCADE)
#     rs = models.ImageField(blank=True)
#     psa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     creatinine = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     wbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     rbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     hemoglobin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     hematocrit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     platelet = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     lactate_hydrogenase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     alkaline_phosphatase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     sgpt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     sgot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     bilirubins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     gapsma = models.OneToOneField(Gapsma, on_delete=models.CASCADE)
#     fdgpetct = models.OneToOneField(Fdgpetct, on_delete=models.CASCADE)
    
    #other lesion!