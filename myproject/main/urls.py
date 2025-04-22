from django.urls import path
from .views import trigger_task

urlpatterns = [
    path('run-task/', trigger_task),
]
