from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import SignUpForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {"form": form})
