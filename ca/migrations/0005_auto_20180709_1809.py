# Generated by Django 2.0.5 on 2018-07-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0004_auto_20180621_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='college',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ca',
            name='comment',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ca',
            name='gender',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ca',
            name='image',
            field=models.FileField(default=11, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ca',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ca',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ca',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
