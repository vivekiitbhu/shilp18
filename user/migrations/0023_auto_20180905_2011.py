# Generated by Django 2.1 on 2018-09-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20180904_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='year',
            field=models.CharField(max_length=300),
        ),
    ]
