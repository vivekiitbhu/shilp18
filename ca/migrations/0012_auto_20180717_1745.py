# Generated by Django 2.0.7 on 2018-07-17 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0011_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='postMessage',
        ),
    ]
