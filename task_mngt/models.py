from django.db import models
from django.contrib.auth.models import User

class Milestone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateField()
    completion_percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class WorkItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=[('p1', 'P1'), ('p2', 'P2'), ('p3', 'P3')], default='p3')
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('inprogress', 'In Progress'), ('blocked', 'Blocked'), ('done', 'Done')], default='new')
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    target_date = models.DateField()

    def __str__(self):
        return self.name

class TaskAssignment(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(WorkItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.assigned_to.username} - {self.task.name}"
