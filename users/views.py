from django.shortcuts import render
from .forms import RegistrationForm


def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        "form": form,
    }

    return render(request, "users/register.html", context)

