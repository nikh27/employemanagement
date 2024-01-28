from django.contrib import admin
from .models import *

admin.site.register(Milestone)
admin.site.register(WorkItem)
admin.site.register(TaskAssignment)