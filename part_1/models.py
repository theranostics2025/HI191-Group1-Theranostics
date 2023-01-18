from django.db import models
from django.utils.text import slugify

class AutoIncrementField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

class Patient(models.Model):
    #Demographic should contain 
    patient_code = AutoIncrementField()
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.patient_code:
            qs = self.__class__.objects.filter(created__year=self.created.year)
            if qs.exists():
                self.patient_code = "{:04d}".format(qs.latest('created').patient_code + 1)
            else:
                self.patient_code = "{:04d}".format(1)
        super(Patient, self).save(*args, **kwargs)