from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    # path('task_management/', task_management, name='task_management'),
    path('', task_management, name='task_management'),
]