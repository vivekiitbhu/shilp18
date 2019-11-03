# Generated by Django 2.0.7 on 2018-09-17 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamid', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('leader_email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
                ('number_members', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20)),
                ('quiz_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Quiz_Team')),
            ],
        ),
    ]
