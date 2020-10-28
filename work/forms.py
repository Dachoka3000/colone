from django import forms
from .models import Project,Profile

class UploadProject(forms.Form):
    class Meta:
        model = Project
        exclude = ['owner','date_added']
