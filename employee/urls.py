from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('emp_home/', emp_home, name='emp_home'),
    path('emp_home/user_management/', user_management, name='user_management'),
    path('emp_home/task_management/', task_management, name='task_management'),
    path('emp_home/report/', report, name='report'),
    path('user_master/', user_master, name='user_master'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('view_user/<int:user_id>/', view_user, name='view_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('department/', department, name='department'),
    path('designation/', designation, name='designation'),
    path('user_menu_permission/', user_menu_permission, name='user_menu_permission'),
]