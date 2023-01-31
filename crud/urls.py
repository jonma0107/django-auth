from django.urls import path
from . import views
from .views import cerrar, abrir, create_task



urlpatterns = [
  path('', views.home, name="home"),
  path('signup/', views.signup, name="signup"),
  path('tasks/', views.tasks, name="tasks"),
  path('tasks/create/', views.create_task, name="create_task"),
  path('logout/', views.cerrar, name="logout"),
  path('signin/', views.abrir, name="signin")
]

