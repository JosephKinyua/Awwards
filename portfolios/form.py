from django import forms
from django.db.models.fields import TextField
from django.forms.fields import ChoiceField
from django.forms.widgets import TextInput
from .models import Projects, Profile
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)
class ProfileForm(forms.ModelForm):
    class Meta:
      model = Profile
      fields = '__all__'
      exclude = ['username', 'count',]
class PostForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'description', 'livelink',)
        exclude = ['projectowner',]
        widgets = {
            'title':TextInput(attrs={
            'placeholder': 'Project Title...',
        }),
        'livelink': TextInput(attrs={
            'placeholder': 'Project live link...',
        })
        }