# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-08-10 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0005_auto_20210810_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
