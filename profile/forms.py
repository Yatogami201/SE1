from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext as _



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Las contraseñas no coinciden."), code='password_mismatch')

        if password2:
            password_validation.validate_password(password2)
        
        return cleaned_data

