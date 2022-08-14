from django.urls import path
from .views import *

app_name = 'task'
urlpatterns = [
    path('create-task/', TaskCreateView.as_view(), name='create_task'),

    path('all-tasks/', TaskListView.as_view(), name='all_tasks'),
    path('all-managers/', ManagerListView.as_view(), name='all_managers'),

    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),

]
