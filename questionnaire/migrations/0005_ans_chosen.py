# Generated by Django 2.0.7 on 2018-09-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20180921_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ans_chosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_id', models.IntegerField()),
                ('ans', models.CharField(max_length=10)),
            ],
        ),
    ]
