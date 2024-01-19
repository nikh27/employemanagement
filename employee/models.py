# models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

class Department(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField(choices=STATUS_CHOICES, default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Designation(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EmployeeDetail(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    
    # ForeignKey relationship with Department for empdept field
    empdept = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    joiningdate = models.DateField(null=True)
    

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
        
    def __str__(self):
        return self.user.username

class UserMenuPermission(models.Model):
    PERMISSION_CHOICES = [
        (True, 'Is Staff'),
        (False, 'Not Staff'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)
    permission_level = models.BooleanField(choices=PERMISSION_CHOICES, default=False)

    def __str__(self):
        return f"{self.user.username} - {self.menu_name} - {'Is Staff' if self.permission_level else 'Not Staff'}"

    def get_permission_display(self):
        return 'Is Staff' if self.permission_level else 'Not Staff'

@receiver(post_save, sender=UserMenuPermission)
def update_user_is_staff(sender, instance, **kwargs):
    instance.user.is_staff = instance.permission_level
    instance.user.save()