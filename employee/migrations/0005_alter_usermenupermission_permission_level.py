# Generated by Django 5.0 on 2024-01-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_usermenupermission_permission_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermenupermission',
            name='permission_level',
            field=models.BooleanField(choices=[(True, 'Is Staff'), (False, 'Not Staff')], default=False),
        ),
    ]
