from django.contrib import admin
from django.urls import path, include
from employee.views import *

urlpatterns = [
    path('', emp_home, name='emp_home'),
    path('task_management/', include('task_mngt.urls')),
    path('report/', report, name='report'),
    path('user_master/', user_master, name='user_master'),
    # User Management URLs
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('view_user/<int:user_id>/', view_user, name='view_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),

    # Department URLs
    path('department/', department, name='department'),
    path('add_department/', add_department, name='add_department'),
    path('edit_department/<int:department_id>/', edit_department, name='edit_department'),
    path('view_department/<int:department_id>/', view_department, name='view_department'),
    path('delete_department/<int:department_id>/', delete_department, name='delete_department'),


    
    path('designations/', designations, name='designations'),
    path('add_designations/', add_designation, name='add_designation'),
    path('edit_designations/<int:designation_id>/', view_designation, name='view_designation'),
    path('view_designations/<int:designation_id>/', edit_designation, name='edit_designation'),
    path('delete_designations/<int:designation_id>/', delete_designation, name='delete_designation'),

    path('user_menu_permission/', user_menu_permission, name='user_menu_permission'),
    path('update_permission/<int:permission_id>/', update_permission, name='update_permission'),
]