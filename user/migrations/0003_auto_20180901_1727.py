# Generated by Django 2.1 on 2018-09-01 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
