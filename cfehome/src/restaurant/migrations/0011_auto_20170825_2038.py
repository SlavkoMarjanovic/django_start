# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_restaurantlocation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='user',
            new_name='owner',
        ),
    ]