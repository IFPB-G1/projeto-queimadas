# Generated by Django 4.0.3 on 2022-05-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queimada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queimada',
            name='acq_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='queimada',
            name='acq_time',
            field=models.TimeField(),
        ),
    ]
