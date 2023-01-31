from django.urls import path
from . import views
from .views import cerrar, abrir



urlpatterns = [
  path('', views.home, name="home"),
  path('signup/', views.signup, name="signup"),
  path('tasks/', views.tasks, name="tasks"),
  path('logout/', views.cerrar, name="logout"),
  path('signin/', views.abrir, name="signin")

]
abrir
