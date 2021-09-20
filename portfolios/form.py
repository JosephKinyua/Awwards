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