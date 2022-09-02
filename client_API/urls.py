from django.urls import path
from .views import *

app_name = 'task'
urlpatterns = ([
    # Create Task
    path('create-task/', TaskCreateView.as_view(), name='create_task'),

    # All Item List
    path('all-tasks/', TaskListView.as_view(), name='all_tasks'),
    path('all-managers/', ManagerListView.as_view(), name='all_managers'),

    # Detail
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),


    # viewsSets
    # path('all-managers/', views.ManagersViewSet.as_view({"get": "list"})),
    # path('manager/<int:pk>/', views.ManagersViewSet.as_view(
    #     {"get":"retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})),
    #
    # path('create-task/', views.TaskViewSet.as_view({"post": "create"})),
    # path('all-tasks/', views.TaskViewSet.as_view({"get": "list"})),
    # path('task/<int:pk>/', views.TaskViewSet.as_view(
    #     {"get":"retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})),

])
