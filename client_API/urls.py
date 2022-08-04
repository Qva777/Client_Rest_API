from django.urls import path
from .views import *

app_name = 'task'
urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('all/', TaskListView.as_view(), name='all'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),

]
