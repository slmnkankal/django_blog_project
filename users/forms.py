from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.changed_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Please use another Email, that one already taken")
        return email

    # def clean_first_name(self):
    #     name = self.cleaned_data["first_name"]
    #     if "a" in name:
    #         raise forms.ValidationError("Your name includes a")
    #     return name

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "bio")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")