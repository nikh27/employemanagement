from django.contrib import admin
from django.urls import path, include
from employee.views import *

urlpatterns = [
    path('', emp_home, name='emp_home'),
    path('user_management/', user_management, name='user_management'),
    path('task_management/', include('task_mngt.urls')),
    path('report/', report, name='report'),
    path('user_master/', user_master, name='user_master'),
    # User Management URLs
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('view_user/<int:user_id>/', view_user, name='view_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),

    # Department URLs
    path('edit_department/<int:department_id>/', edit_department, name='edit_department'),
    path('view_department/<int:department_id>/', view_department, name='view_department'),
    path('delete_department/<int:department_id>/', delete_department, name='delete_department'),
    path('add_department/', add_department, name='add_department'),
    
    path('department/', department, name='department'),
    path('designation/', designation, name='designation'),
    path('user_menu_permission/', user_menu_permission, name='user_menu_permission'),
]