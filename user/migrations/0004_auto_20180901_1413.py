# Generated by Django 2.0.7 on 2018-09-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180901_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='accomodation',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='delta',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='enviro',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='icreate',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='mudmarine',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='nirman',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='num_events',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='paper_presentation',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='questionnaire',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='this_or_that_way',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
