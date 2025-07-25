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
            'salivary_gland': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}), 
            'kidney_left': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}), 
            'kidney_right': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}) 
        }
        labels = {
            'date_of_post_therapy': 'Date of Post Therapy',
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in hours)',
            'bone_lesion_details': 'Bone Lesion Details',
            'lesion_image': 'Lesion Image',
            'salivary_gland': 'Salivary Gland', 
            'kidney_left': 'Kidney Left', 
            'kidney_right': 'Kidney Right',
        }

class EditPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
            'salivary_gland': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}), 
            'kidney_left': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}), 
            'kidney_right': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}) 
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)',
            'bone_lesion_details': 'Bone Lesion Details',
            'lesion_image': 'Lesion Image',
            'salivary_gland': 'Salivary Gland', 
            'kidney_left': 'Kidney Left', 
            'kidney_right': 'Kidney Right',
        }