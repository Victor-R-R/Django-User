from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


def signup(request):
    context = {}
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Bienvenue !")
        else:
            context["errors"] = form.errors

    form = UserCreationForm()
    context["form"] = form
    return render(request, "signup.html", context=context)
