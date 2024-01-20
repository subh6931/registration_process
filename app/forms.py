from django import forms
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':''}
class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']