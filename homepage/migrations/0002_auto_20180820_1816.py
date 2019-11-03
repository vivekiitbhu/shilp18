# Generated by Django 2.0.7 on 2018-08-20 18:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', ckeditor.fields.RichTextField()),
                ('rank', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Event')),
            ],
            options={
                'ordering': ('rank',),
            },
        ),
        migrations.RemoveField(
            model_name='eventdetails',
            name='event',
        ),
        migrations.DeleteModel(
            name='EventDetails',
        ),
    ]
