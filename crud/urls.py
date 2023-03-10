from django.urls import path
from . import views
from .views import close_sesion, open_sesion, create_task, task_detail, task_done, delete_task_completed


urlpatterns = [
  path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/completed', views.tasks_completed, name="tasks_completed"),
    path('tasks/create/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('tasks/<int:task_id>/done/', views.task_done, name="task_done"),
    path('tasks/<int:task_id>/delete_task_completed/', views.delete_task_completed, name="delete_task_completed"),
    path('logout/', views.close_sesion, name="logout"),
    path('signin/', views.open_sesion, name="signin")
]

