from atexit import register
from django.contrib import admin
from .models import Profile, user_profile_path

admin.site.register(Profile)

# Register your models here.
