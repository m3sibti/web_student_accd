from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    u_type = forms.CharField(max_length=30, required=True, help_text='MUST')

    class Meta:
        model = get_user_model()
        fields = ["first_name", "username", "email", "password1", "password2", "u_type"]
