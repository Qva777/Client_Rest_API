from django.urls import path
from .views import *
from .yasg import urlpatterns as doc_urls

app_name = 'task'
urlpatterns = [
    # Create Task
    path('create-task/', TaskCreateView.as_view(), name='create_task'),

    # All Item List
    path('all-tasks/', TaskListView.as_view(), name='all_tasks'),
    path('all-managers/', ManagerListView.as_view(), name='all_managers'),

    # Detail
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),
]

urlpatterns += doc_urls

