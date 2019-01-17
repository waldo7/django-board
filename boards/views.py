from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Board
# Create your views here.


class HomeView(ListView):
    model = Board
    context_object_name = "boards"
    template_name = "boards/home.html"


class TopicsListing(DetailView):
    model = Board
    template_name = "boards/topics.html"
    context_object_name = "board"
