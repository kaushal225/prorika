from django.forms import ModelForm
from .models import Problem

class ProblemForm(ModelForm):
    
    class Meta:
       model=Problem
       fields=['name','description','is_completed','website']