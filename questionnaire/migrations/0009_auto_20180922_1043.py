# Generated by Django 2.0.7 on 2018-09-22 10:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_quiz_team_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ques',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
