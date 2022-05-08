from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'image',
            'title',
            'patternlnk',
            'yarn',
            'meters',
            'dateStart',
            'dateDone',
            'description',
        )

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',

        ]

