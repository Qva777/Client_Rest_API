from django.urls import path
from client_API import views

app_name = 'task'
http_request = {"put": "update",  "patch": "partial_update", "delete": "destroy"}
urlpatterns = ([
    # viewsSets
    path('create-task/', views.TaskViewSet.as_view({"post": "create"})),

    path('task/<int:pk>/', views.TaskViewSet.as_view({"get": "retrieve"})),
    path('manager/<int:pk>/', views.ManagersViewSet.as_view({"get": "retrieve"})),

    path('task/put/<int:pk>/', views.TaskViewSet.as_view(http_request)),
    path('manager/put/<int:pk>/', views.ManagersViewSet.as_view(http_request)),

    path('all-tasks/', views.TaskViewSet.as_view({"get": "list"})),
    path('all-managers/', views.ManagersViewSet.as_view({"get": "list"})),

])
