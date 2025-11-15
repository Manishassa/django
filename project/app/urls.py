from django.urls import path
from . import views

urlpatterns = [
    path("chain", views.view_logic, name='index'),
]
