# Generated by Django 5.0 on 2023-12-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0002_rename_brand_car_marque_remove_car_displacement'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='note',
            field=models.FloatField(default=0.0),
        ),
    ]
