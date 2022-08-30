from django.urls import path
from .views import *

# viewset
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'task'
urlpatterns = format_suffix_patterns([
    path('create-task/', TaskCreateView.as_view(), name='create_task'),

    path('all-tasks/', TaskListView.as_view(), name='all_tasks'),
    path('all-managers/', ManagerListView.as_view(), name='all_managers'),

    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),
    path('manager/put/<int:pk>/', ManagerDetailViewUpdate.as_view(), name='manager_detail_update'),
    # viewsSets
    # path('all-managers/', views.ManagersViewSet.as_view({"get": "list"})),
    # path('manager/<int:pk>/', views.ManagersViewSet.as_view({"put": "retrieve"}), name='manager_detail'),
    # path('manager/put/<int:pk>/', views.ManagersViewSet.as_view({"put": "retrieve"}), name='manager_detail_update'),

])
