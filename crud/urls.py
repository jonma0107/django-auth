from django.urls import path
from . import views
from .views import close_sesion, open_sesion, create_task, task_detail, completed_task


urlpatterns = [
  path('', views.home, name="home"),
  path('signup/', views.signup, name="signup"),
  path('tasks/', views.tasks, name="tasks"),
  path('tasks/create/', views.create_task, name="create_task"),
  path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
  path('tasks/<int:task_id>/complete/', views.completed_task, name="completed_task"),
  path('logout/', views.close_sesion, name="logout"),
  path('signin/', views.open_sesion, name="signin")
]

