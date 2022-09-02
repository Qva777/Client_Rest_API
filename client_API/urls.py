from django.urls import path

from client_API import views
from .views import *

# viewset
# from client_API.views import ManagersViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'users', ManagersViewSet, basename='manager')
# urlpatterns = router.urls

app_name = 'task'
urlpatterns = ([
    path('create-task/', TaskCreateView.as_view(), name='create_task'),

    path('all-tasks/', TaskListView.as_view(), name='all_tasks'),
    path('all-managers/', ManagerListView.as_view(), name='all_managers'),

    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),
    # path('manager/put/<int:pk>/', ManagerDetailViewUpdate.as_view(), name='manager_detail_update'),


    # viewsSets
    # path('all-managers/', views.ManagersViewSet.as_view({"get": "list"})),
    # path('manager/<int:pk>/', views.ManagersViewSet.as_view(
    #     {"put": "update"}))#, "head": "", "options": ""})),
    # path('manager/put/<int:pk>/', views.ManagersViewSet.as_view({"put": "retrieve"})),

])
