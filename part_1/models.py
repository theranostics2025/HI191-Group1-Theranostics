from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class AutoIncrementField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

class PhysicalExam(models.Model):
    
    ecog_score = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    bmi = models.IntegerField(blank=True) # Body Mass Index
    bp = models.IntegerField(blank=True) # Blood Pressure
    hr = models.IntegerField(blank=True) # Heart Rate
    pain_score = models.IntegerField(min_value=0, max_value = 10, blank=True)
    local_symptoms = models.CharField(max_length=300, blank=True)
    systemic_symptoms = models.CharField(max_length=300, blank=True)

class SalivaryGland(models.Model):
    STATUS = (
        ('Normal', 'Normal'),
        ('Left Obstruction', 'Left Obstruction'),
        ('Right Obstruction', 'Right Obstruction')
    )
    status = models.CharField(choices = STATUS)
    sg_image = models.ImageField(blank=True)

class BoneScan(models.Model):
    METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    metastasis_status = models.CharField(choices = METASTASIS_STATUS)
    sg_image = models.ImageField()

class Lesion(models.Model):
    LESION_STATUS = (
        ('Absent', 'Absent'),
        ('Present', 'Present')
    )
    lesion_status = models.CharField(choices = LESION_STATUS)
    location = models.CharField(max_length=50, null=True, blank=True)
    suv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    size = models.IntegerField(blank=True)

class Gapsma(models.Model):
    CHOICES = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    choices = models.CharField(choices=CHOICES)
    gapsma_img = models.ImageField(blank=True)
    prostate_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    lymph_node_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    bone_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    brain_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    lung_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    liver_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)

class Fdgpetct(models.Model):
    fdgpetct_img = models.ImageField(blank=True)
    prostate_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    lymph_node_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    bone_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    brain_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    lung_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)
    liver_lesion = models.OneToOneField(Lesion, on_delete=models.CASCADE)

class Screening(models.Model):
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    salivarygland = models.OneToOneField(SalivaryGland, on_delete=models.CASCADE)
    bonescan = models.OneToOneField(BoneScan, on_delete=models.CASCADE)
    rs = models.ImageField(blank=True)
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
    gapsma = models.OneToOneField(Gapsma, on_delete=models.CASCADE)
    fdgpetct = models.OneToOneField(Fdgpetct, on_delete=models.CASCADE)
    
    #other lesion!

class Patient(models.Model):
    TYPE_TREATMENT = (
        ('Hormonal Treatment', 'Hormonal Treatment'),
        ('Radiation Therapy', 'Radiation Therapy'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Others', 'Others'),
    )
    #Test results and others are put to a different model
    name = models.CharField(max_length=120, blank= False, null=True)
    patient_code = AutoIncrementField()
    age = models.IntegerField()
    address = models.CharField(max_length=300)
    diagnosis_date = models.DateField()
    surgery_date = models.DateField()
    histopath_result = models.ImageField()
    gleason_score = models.IntegerField
    date_of_treatment = models.DateField()
    type_of_treatment = models.CharField(choices=TYPE_TREATMENT)
    physical_exam = models.OneToOneField(PhysicalExam, on_delete=models.CASCADE)
    def __str__(self): 
        return self.name

    def save(self, *args, **kwargs):
        if not self.patient_code:
            qs = self.__class__.objects.filter(created__year=self.created.year)
            if qs.exists():
                self.patient_code = "{:04d}".format(qs.latest('created').patient_code + 1)
            else:
                self.patient_code = "{:04d}".format(1)
        super(Patient, self).save(*args, **kwargs)

