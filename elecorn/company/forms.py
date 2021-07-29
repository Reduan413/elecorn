from .models import *
from django import forms
import datetime

class UnitManagerForm(forms.ModelForm):
 
    code = forms.CharField(max_length=3, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=30,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Unit_Manager
        fields = '__all__'