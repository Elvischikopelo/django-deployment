from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import CreateView

class SignUp(CreateView):
    form_class = UserCreateForm 