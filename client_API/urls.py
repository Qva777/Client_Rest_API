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

    # Update
    path('task/put/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('manager/put/<int:pk>/', ManagerUpdateSerializersViews.as_view(), name='manager_update'),

]


urlpatterns += doc_urls

