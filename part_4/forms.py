from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddFollowUp(ModelForm):
    class Meta:
        model = FollowUp
        fields = ['date_of_follow_up', 'psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
        'salivary_gland_status', 'salivary_gland_image', 'bone_metastasis_status', 'bone_scan_image', 'renal_scintigraphy', 'gapsma_choices', 'gapsma_img', 
        'gapsma_prostate_lesion_status', 'gapsma_prostate_location', 'gapsma_prostate_suv', 'gapsma_prostate_size',
        'gapsma_lymph_node_lesion_status', 'gapsma_lymph_node_location', 'gapsma_lymph_node_suv', 'gapsma_lymph_node_size',
        'gapsma_bone_lesion_status', 'gapsma_bone_location', 'gapsma_bone_suv', 'gapsma_bone_size',
        'gapsma_brain_lesion_status', 'gapsma_brain_location', 'gapsma_brain_suv', 'gapsma_brain_size',
        'gapsma_lung_lesion_status', 'gapsma_lung_location', 'gapsma_lung_suv', 'gapsma_lung_size',
        'gapsma_liver_lesion_status', 'gapsma_liver_lesion_status', 'gapsma_liver_location', 'gapsma_liver_suv', 'gapsma_liver_size',
        'fdgpetct_img',
        'fdgpetct_prostate_lesion_status', 'fdgpetct_prostate_location', 'fdgpetct_prostate_suv', 'fdgpetct_prostate_size',
        'fdgpetct_lymph_node_lesion_status', 'fdgpetct_lymph_node_location', 'fdgpetct_lymph_node_suv', 'fdgpetct_lymph_node_size',
        'fdgpetct_bone_lesion_status', 'fdgpetct_bone_location', 'fdgpetct_bone_suv', 'fdgpetct_bone_size',
        'fdgpetct_brain_lesion_status', 'fdgpetct_brain_location', 'fdgpetct_brain_suv', 'fdgpetct_brain_size',
        'fdgpetct_lung_lesion_status', 'fdgpetct_lung_location', 'fdgpetct_lung_suv', 'fdgpetct_lung_size',
        'fdgpetct_liver_lesion_status', 'fdgpetct_liver_location', 'fdgpetct_liver_suv', 'fdgpetct_liver_size',
        'assessment', 'plan']

        widgets = {
            'date_of_follow_up': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'psa': 'PSA',
            'creatinine': 'Creatinine(mg/dL)',
            'wbc': 'WBC',
            'rbc' : 'RBC',
            'hemoglobin' : 'Hemogoblin(g/dL)',
            'hematocrit' : 'Hematocrit(%)',
            'platelet' : 'Platelet Count(mcL)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase(units/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase(units/L)', 
            'sgpt' : 'SGPT(units/L)', 
            'sgot' : 'SGOT(units/L)', 
            'bilirubins' : 'Bilirubins(mg/dL)',
        }

class EditFollowUp(ModelForm):
    class Meta:
        model = FollowUp
        fields = ['date_of_follow_up', 'psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
        'salivary_gland_status', 'salivary_gland_image', 'bone_metastasis_status', 'bone_scan_image', 'renal_scintigraphy', 'gapsma_choices', 'gapsma_img', 
        'gapsma_prostate_lesion_status', 'gapsma_prostate_location', 'gapsma_prostate_suv', 'gapsma_prostate_size',
        'gapsma_lymph_node_lesion_status', 'gapsma_lymph_node_location', 'gapsma_lymph_node_suv', 'gapsma_lymph_node_size',
        'gapsma_bone_lesion_status', 'gapsma_bone_location', 'gapsma_bone_suv', 'gapsma_bone_size',
        'gapsma_brain_lesion_status', 'gapsma_brain_location', 'gapsma_brain_suv', 'gapsma_brain_size',
        'gapsma_lung_lesion_status', 'gapsma_lung_location', 'gapsma_lung_suv', 'gapsma_lung_size',
        'gapsma_liver_lesion_status', 'gapsma_liver_lesion_status', 'gapsma_liver_location', 'gapsma_liver_suv', 'gapsma_liver_size',
        'fdgpetct_img',
        'fdgpetct_prostate_lesion_status', 'fdgpetct_prostate_location', 'fdgpetct_prostate_suv', 'fdgpetct_prostate_size',
        'fdgpetct_lymph_node_lesion_status', 'fdgpetct_lymph_node_location', 'fdgpetct_lymph_node_suv', 'fdgpetct_lymph_node_size',
        'fdgpetct_bone_lesion_status', 'fdgpetct_bone_location', 'fdgpetct_bone_suv', 'fdgpetct_bone_size',
        'fdgpetct_brain_lesion_status', 'fdgpetct_brain_location', 'fdgpetct_brain_suv', 'fdgpetct_brain_size',
        'fdgpetct_lung_lesion_status', 'fdgpetct_lung_location', 'fdgpetct_lung_suv', 'fdgpetct_lung_size',
        'fdgpetct_liver_lesion_status', 'fdgpetct_liver_location', 'fdgpetct_liver_suv', 'fdgpetct_liver_size',
        'assessment', 'plan']

        widgets = {
            'date_of_follow_up': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'psa': 'PSA',
            'creatinine': 'Creatinine(mg/dL)',
            'wbc': 'WBC',
            'rbc' : 'RBC',
            'hemoglobin' : 'Hemogoblin(g/dL)',
            'hematocrit' : 'Hematocrit(%)',
            'platelet' : 'Platelet Count(mcL)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase(units/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase(units/L)', 
            'sgpt' : 'SGPT(units/L)', 
            'sgot' : 'SGOT(units/L)', 
            'bilirubins' : 'Bilirubins(mg/dL)',
        }
        