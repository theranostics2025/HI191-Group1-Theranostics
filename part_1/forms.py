from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field

# ADDING DATA
class AddPatient(ModelForm):
    def __init__(self, *args1, **args2):
        super().__init__(*args1, **args2)
        self.fields['name'].label = "Name"
        self.fields['age'].label = "Age"
        self.fields['address'].label = "Address"
        self.fields['diagnosis_date'].label = "Diagnosis Date"
        self.fields['surgery_date'].label = "Surgery Date"
        self.fields['histopath_result'].label = "Histopathology Result"
        self.fields['histopath_details'].label = "Histopathology Details"
        self.fields['gleason_score'].label = "Gleason Score"
        self.fields['date_of_treatment'].label = "Date of Treatment"
        self.fields['type_of_treatment'].label = "Type of Treatment"

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age

    class Meta:
        model = Patient
        fields = [
            'name',
            'age',
            'address',
            'diagnosis_date',
            'surgery_date',
            'histopath_result',
            'histopath_details',
            'gleason_score',
            'date_of_treatment',
            'type_of_treatment'
        ]
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'step': '1', 'min': '0', 'type': 'number'}),
            'gleason_score': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'name': {'required': "Patient name is required."},
            'age': {'required': "Patient age is required.", 'invalid': "Please enter a valid age."},
            'address': {'required': "Address is required."},
            'diagnosis_date': {'required': "Diagnosis date is required."},
            'surgery_date': {'required': "Surgery date is required."},
            'histopath_result': {'required': "Histopathology result image is required."},
            'histopath_details': {'required': "Histopathology details are required."},
            'gleason_score': {'invalid': "Please select a valid Gleason score."},
            'date_of_treatment': {'required': "Treatment date is required."},
            'type_of_treatment': {'required': "Type of treatment is required."}
        }

class EditPatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        }

class PhysicalExamFormBase(ModelForm):
    def __init__(self, *args1, **args2):
        super().__init__(*args1, **args2)
        self.helper = FormHelper()
        self.helper.form_tag = False 
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = PhysicalExam
        fields = ['ecog_score', 'height', 'weight', 'bmi', 'bp', 'hr', 'pain_score', 'local_symptoms', 'systemic_symptoms']
        labels = {
            'ecog_score': 'ECOG Performance Status Score',
            'height': 'Height (cm)',
            'weight': 'Weight (kg)',
            'bmi': 'Body Mass Index (BMI) (kg/m²)',
            'bp': 'Blood Pressure (mmHg)',
            'hr': 'Heart Rate (bpm)',
            'pain_score': 'Pain Score',
            'local_symptoms': 'Local Symptoms',
            'systemic_symptoms': 'Systemic Symptoms',
        }
        widgets = {
            'ecog_score': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'bmi': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'step': '0.01'}),
            'bp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'systolic/diastolic (i.e. 120/80)',
                                         'onkeypress': (
                                                "if (event.charCode === 47 && this.value.includes('/')) return false; "
                                                "return (event.charCode === 0 || (event.charCode >= 48 && event.charCode <= 57) || event.charCode === 47);"
                                            )}),
            'hr': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
            'pain_score': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0', 'max': '10', 'placeholder': '0 (no pain) to 10 (worst pain)'}),
            'local_symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'systemic_symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        
    def clean_ecog_score(self):
        ecog_score = self.cleaned_data.get('ecog_score')
        try:
            ecog_score = int(ecog_score) if ecog_score is not None else None
            if ecog_score is not None and not (0 <= ecog_score <= 5):
                raise forms.ValidationError("Please select a score from 0 to 5.")
        except (ValueError, TypeError):
            raise forms.ValidationError("ECOG score must be a number between 0 and 5.")
        return ecog_score
    
    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and height <= 0:
            raise forms.ValidationError("Height must be a non-negative value.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise forms.ValidationError("Weight must be a non-negative value.")
        return weight

    def clean_hr(self):
        hr = self.cleaned_data.get('hr')
        if hr is not None and hr <= 0:
            raise forms.ValidationError("Heart rate must be a non-negative value.")
        return hr
    
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
    
    def clean_pain_score(self):
        pain_score = self.cleaned_data.get('pain_score')
        if pain_score is not None and not (0 <= pain_score <= 10):
            raise forms.ValidationError("Pain score must be between 0 and 10.")
        return pain_score

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class EditPhysicalExam(PhysicalExamFormBase):
    pass

class AddPhysicalExam(PhysicalExamFormBase):
    pass

class AddScreening(ModelForm):
    def clean_psa(self):
        psa = self.cleaned_data.get('psa')
        if psa is not None and psa < 0:
            raise forms.ValidationError("PSA must be a non-negative value.")
        return psa

    def clean_creatinine(self):
        creatinine = self.cleaned_data.get('creatinine')
        if creatinine is not None and creatinine < 0:
            raise forms.ValidationError("Creatinine must be a non-negative value.")
        return creatinine

    def clean_wbc(self):
        wbc = self.cleaned_data.get('wbc')
        if wbc is not None and wbc < 0:
            raise forms.ValidationError("WBC must be a non-negative value.")
        return wbc

    def clean_rbc(self):
        rbc = self.cleaned_data.get('rbc')
        if rbc is not None and rbc < 0:
            raise forms.ValidationError("RBC must be a non-negative value.")
        return rbc

    def clean_hemoglobin(self):
        hemoglobin = self.cleaned_data.get('hemoglobin')
        if hemoglobin is not None and hemoglobin < 0:
            raise forms.ValidationError("Hemoglobin must be a non-negative value.")
        return hemoglobin

    def clean_hematocrit(self):
        hematocrit = self.cleaned_data.get('hematocrit')
        if hematocrit is not None and hematocrit < 0:
            raise forms.ValidationError("Hematocrit must be a non-negative value.")
        return hematocrit

    def clean_platelet(self):
        platelet = self.cleaned_data.get('platelet')
        if platelet is not None and platelet < 0:
            raise forms.ValidationError("Platelet count must be a non-negative value.")
        return platelet

    def clean_lactate_hydrogenase(self):
        lactate_hydrogenase = self.cleaned_data.get('lactate_hydrogenase')
        if lactate_hydrogenase is not None and lactate_hydrogenase < 0:
            raise forms.ValidationError("Lactate Hydrogenase must be a non-negative value.")
        return lactate_hydrogenase

    def clean_alkaline_phosphatase(self):
        alkaline_phosphatase = self.cleaned_data.get('alkaline_phosphatase')
        if alkaline_phosphatase is not None and alkaline_phosphatase < 0:
            raise forms.ValidationError("Alkaline Phosphatase must be a non-negative value.")
        return alkaline_phosphatase

    def clean_sgpt(self):
        sgpt = self.cleaned_data.get('sgpt')
        if sgpt is not None and sgpt < 0:
            raise forms.ValidationError("SGPT must be a non-negative value.")
        return sgpt

    def clean_sgot(self):
        sgot = self.cleaned_data.get('sgot')
        if sgot is not None and sgot < 0:
            raise forms.ValidationError("SGOT must be a non-negative value.")
        return sgot

    def clean_bilirubins(self):
        bilirubins = self.cleaned_data.get('bilirubins')
        if bilirubins is not None and bilirubins < 0:
            raise forms.ValidationError("Bilirubins must be a non-negative value.")
        return bilirubins

    class Meta:
        model = Screening
        fields = ['psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
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
            'salivary_gland_status' : 'Salivary Gland Status',
            'salivary_gland_image' : 'Salivary Gland Image',
            'bone_metastasis_status' : 'Bone Metastasis Status',
            'bone_scan_image' : 'Bone Scan Image',
            'renal_scintigraphy' : 'Renal Scintigraphy',
            'gapsma_choices' : 'GAPSMA Choices',
            'gapsma_img' : 'GAPSMA Image',
            'fdgpetct_img' : 'FDG-PET/CT Image',
        }
        widgets = {
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

class EditScreening(AddScreening):
    def __init__(self, *args1, **args2):
        super().__init__(*args1, **args2)
        
    class Meta(AddScreening.Meta):
        model = Screening