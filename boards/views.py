from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Board
# Create your views here.


def home(request):
    return HttpResponse("hello")


class HomeView(ListView):
    model = Board
    context_object_name = "boards"
    template_name = "boards/home.html"
