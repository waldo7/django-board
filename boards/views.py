from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, View

from .models import Board, Topic, Post

# Create your views here.


class HomeView(ListView):
    model = Board
    context_object_name = "boards"
    template_name = "boards/home.html"


class TopicsListing(DetailView):
    model = Board
    template_name = "boards/topics.html"
    context_object_name = "board"


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)
    return render(request, 'boards/new_topic.html', {'board': board})
