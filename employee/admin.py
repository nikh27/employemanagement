from django.contrib import admin
from .models import *

admin.site.register(EmployeeDetail)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(UserMenuPermission)