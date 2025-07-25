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
            'psa': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'creatinine': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'wbc': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'rbc': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'hemoglobin': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'hematocrit': forms.NumberInput(attrs={'min': '0', 'max': '100', 'step': '0.01'}),
            'platelet': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'sgpt': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'sgot': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'bilirubins': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            
            # SUV fields with specific validation
            'gapsma_prostate_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),

            # size fields with specific validation
            'gapsma_prostate_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
        }
        labels = {
            'psa': 'PSA (ng/mL)',
            'creatinine': 'Creatinine (mg/dL)',
            'wbc': 'WBC (billion cells/L)',
            'rbc' : 'RBC (trillion cells/L)',
            'hemoglobin' : 'Hemogoblin (g/L)',
            'hematocrit' : 'Hematocrit (%)',
            'platelet' : 'Platelet Count (billion/L)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase (IU/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase (IU/L)', 
            'sgpt' : 'SGPT (U/L)', 
            'sgot' : 'SGOT (U/L)', 
            'bilirubins' : 'Bilirubins (mg/dL)',
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
            'psa': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'creatinine': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'wbc': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'rbc': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'hemoglobin': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'hematocrit': forms.NumberInput(attrs={'min': '0', 'max': '100', 'step': '0.01'}),
            'platelet': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'sgpt': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'sgot': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'bilirubins': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            
            # SUV fields with specific validation
            'gapsma_prostate_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),

            # size fields with specific validation
            'gapsma_prostate_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
        }
        labels = {
            'psa': 'PSA (ng/mL)',
            'creatinine': 'Creatinine (mg/dL)',
            'wbc': 'WBC (billion cells/L)',
            'rbc' : 'RBC (trillion cells/L)',
            'hemoglobin' : 'Hemogoblin (g/L)',
            'hematocrit' : 'Hematocrit (%)',
            'platelet' : 'Platelet Count (billion/L)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase (IU/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase (IU/L)', 
            'sgpt' : 'SGPT (U/L)', 
            'sgot' : 'SGOT (U/L)', 
            'bilirubins' : 'Bilirubins (mg/dL)',
        }
        