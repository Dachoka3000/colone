from django import forms
from .models import Project,Profile,Rating

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner','date_added']

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['project','human']
