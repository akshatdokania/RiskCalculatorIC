# Generated by Django 3.0.8 on 2020-09-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_auto_20200919_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='abg',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='absolute',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='cpk',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='crp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='ctscan',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='ddimer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='ferr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='ldh',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='tropo',
            field=models.FloatField(null=True),
        ),
    ]
