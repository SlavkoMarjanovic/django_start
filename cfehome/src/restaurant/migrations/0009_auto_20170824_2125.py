# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import restaurant.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_restaurantlocation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurant.validators.validate_category]),
        ),
    ]
