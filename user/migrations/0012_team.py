# Generated by Django 2.0.7 on 2018-09-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20180902_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('member1', models.CharField(max_length=100)),
                ('member2', models.CharField(max_length=100)),
                ('member3', models.CharField(max_length=100)),
                ('member4', models.CharField(max_length=100)),
                ('member5', models.CharField(max_length=100)),
                ('member6', models.CharField(max_length=100)),
            ],
        ),
    ]