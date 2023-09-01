from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddTherapy(ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma','premedications','medications','furosemide','systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'date_of_psma' : 'Date of PSMA',
            'systolic' : 'Systolic BP(mmHg)',
            'diastolic' : 'Diastolic BP(mmHg)',
            'hr' : 'Heart Rate(bpm)',
            'rr' : 'Respiratory Rate(bpm)',
            'saturation' : 'Oxygen Saturation(%)'
        }

class EditTherapy(ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma','premedications','medications','furosemide','systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'date_of_psma' : 'Date of PSMA',
            'systolic' : 'Systolic BP(mmHg)',
            'diastolic' : 'Diastolic BP(mmHg)',
            'hr' : 'Heart Rate(bpm)',
            'rr' : 'Respiratory Rate(bpm)',
            'saturation' : 'Oxygen Saturation(%)'
        }
