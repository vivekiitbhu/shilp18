# Generated by Django 2.0.7 on 2018-09-04 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20180904_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='event_paper_presentation',
            new_name='event_colloquiom',
        ),
    ]
