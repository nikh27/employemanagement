# forms.py
from django import forms
from .models import EmployeeDetail,Department
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ['empcode', 'empdept', 'designation', 'contact', 'gender']

    # If you want to customize form fields or add validation, you can do so here
    # For example, you can add a DateInput widget for the joiningdate field:
    widgets = {
        'joiningdate': forms.DateInput(attrs={'type': 'date'}),
    }
    
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description', 'status']