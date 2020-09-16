# Generated by Django 3.0.8 on 2020-09-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('age', models.IntegerField()),
                ('hpd', models.BooleanField()),
                ('ckd', models.BooleanField()),
                ('dm', models.BooleanField()),
                ('htn', models.BooleanField()),
                ('hiv', models.BooleanField()),
                ('trans', models.BooleanField()),
                ('resprate', models.IntegerField()),
                ('heartrate', models.IntegerField()),
                ('spo', models.IntegerField()),
                ('ddimer', models.IntegerField()),
                ('cpk', models.IntegerField()),
                ('crp', models.IntegerField()),
                ('ldh', models.IntegerField()),
                ('tropo', models.FloatField()),
                ('ferr', models.IntegerField()),
                ('absolute', models.FloatField()),
                ('ctscan', models.IntegerField()),
                ('abg', models.IntegerField()),
            ],
        ),
    ]
