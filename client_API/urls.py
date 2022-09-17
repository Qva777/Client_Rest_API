from rest_framework.routers import DefaultRouter
from client_API import views

app_name = 'task'

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')
router.register(r'manager', views.ManagersViewSet, basename='managers')

urlpatterns = ([
    *router.urls,
])
