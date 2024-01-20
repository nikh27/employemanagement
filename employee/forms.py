# forms.py
from django import forms
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ['empcode', 'empdept', 'designation', 'contact', 'gender']
    widgets = {
        'joiningdate': forms.DateInput(attrs={'type': 'date'}),
    }
    
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description', 'status']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name', 'description', 'status']