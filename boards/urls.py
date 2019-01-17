from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('boards/<int:pk>/', views.TopicsListing.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
]
