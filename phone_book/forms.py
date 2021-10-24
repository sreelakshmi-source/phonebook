from . models import *
from django import forms

class updateForms(forms.ModelForm):
    class Meta:
        model=phonebook
        fields=['name','phonenum','address','email']