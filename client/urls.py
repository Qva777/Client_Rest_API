from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'task'
urlpatterns = [
    path('create/', TaskCreateView.as_view()),
    path('all/', TaskListView.as_view()),
    path('api/<int:pk>/', TaskDetailView.as_view()),

]