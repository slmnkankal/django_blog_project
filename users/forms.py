from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.changed_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Please use another Email, that one already taken")
        return email