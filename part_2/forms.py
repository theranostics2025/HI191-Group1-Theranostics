from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddTherapy(ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma','premedications','medications','furosemide','bp', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
            'bp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'systolic/diastolic (i.e. 120/80)',
                                'onkeypress': (
                                    "if (event.charCode === 47 && this.value.includes('/')) return false; "
                                    "return (event.charCode === 0 || (event.charCode >= 48 && event.charCode <= 57) || event.charCode === 47);"
                                )}),
            'hr': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
            'rr': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
            'saturation': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '100'}),
        }

        labels = {
            'date_of_psma' : 'Date of PSMA',
            'bp': 'Blood Pressure (mmHg)',
            'hr' : 'Heart Rate (bpm)',
            'rr' : 'Respiratory Rate (breaths/min)',
            'saturation' : 'Oxygen Saturation (%)',
            'side_effects': 'Side Effects'
        }

    def clean_bp(self):
        bp = self.cleaned_data.get('bp')
        if bp:
            # Validate blood pressure format (e.g., "120/80")
            try:
                systolic, diastolic = bp.split('/')
                systolic = int(systolic)
                diastolic = int(diastolic)
            except ValueError:
                raise forms.ValidationError("Blood pressure must be in format 'systolic/diastolic' (e.g. 120/80)")
        return bp

class EditTherapy(ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma','premedications','medications','furosemide','bp', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
            'bp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'systolic/diastolic (i.e. 120/80)',
                                'onkeypress': (
                                    "if (event.charCode === 47 && this.value.includes('/')) return false; "
                                    "return (event.charCode === 0 || (event.charCode >= 48 && event.charCode <= 57) || event.charCode === 47);"
                                )}),
            'hr': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
            'rr': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
            'saturation': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '100'}),
        }

        labels = {
            'date_of_psma' : 'Date of PSMA',
            'bp': 'Blood Pressure (mmHg)',
            'hr' : 'Heart Rate (bpm)',
            'rr' : 'Respiratory Rate (breaths/min)',
            'saturation' : 'Oxygen Saturation (%)',
            'side_effects': 'Side Effects'
        }

    def clean_bp(self):
        bp = self.cleaned_data.get('bp')
        if bp:
            # Validate blood pressure format (e.g., "120/80")
            try:
                systolic, diastolic = bp.split('/')
                systolic = int(systolic)
                diastolic = int(diastolic)
            except ValueError:
                raise forms.ValidationError("Blood pressure must be in format 'systolic/diastolic' (e.g. 120/80)")
        return bp
