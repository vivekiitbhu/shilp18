# Generated by Django 2.0.7 on 2018-09-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_team_member_mail_sent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz_team',
            options={'ordering': ('-teamid',)},
        ),
    ]
