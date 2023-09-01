from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }

class EditPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }