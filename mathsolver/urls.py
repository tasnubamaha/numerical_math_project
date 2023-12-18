from django.urls import path
from . import views

app_name = 'mathsolver'

urlpatterns = [
    path("home", views.math_problem_solver, name ="home")
]

