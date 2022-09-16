from rest_framework import routers
from django.urls import path
from rest_framework.routers import DefaultRouter

from client_API import views

app_name = 'task'
# http_request = {"put": "update",  "patch": "partial_update", "delete": "destroy"}

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')
router.register(r'manager', views.ManagersViewSet, basename='managers')

urlpatterns = ([
    *router.urls,
])
