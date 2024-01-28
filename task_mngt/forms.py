from django import forms
from .models import *

class MilestoneForm(forms.ModelForm):
    
    class Meta:
        model = Milestone
        fields = ("name","description","target_date","completion_percentage")
