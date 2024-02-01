from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', task_management, name='task_management'),
    path('milestone/', milestone, name='milestone'),
    path('delete_milestone/<int:milestone_id>/', delete_milestone, name='delete_milestone'),
    path('edit_milestone/<int:milestone_id>/', edit_milestone, name='edit_milestone'),

    path('create_task/', create_task, name='create_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),

    path('assign_task/', assign_task, name='assign_task'),
    path('delete_assignment/<int:assignment_id>/', delete_assignment, name='delete_assignment'),
    path('update_assign/<int:assignment_id>/', update_assign, name='update_assign'),
    
    path('my_task/',my_task, name='my_task'),
]