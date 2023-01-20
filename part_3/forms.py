from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan','furosemide','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
