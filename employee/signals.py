# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import UserMenuPermission

# @receiver(post_save, sender=UserMenuPermission)
# def update_user_is_staff(sender, instance, **kwargs):
#     instance.user.is_staff = instance.is_staff_permission
#     instance.user.save()