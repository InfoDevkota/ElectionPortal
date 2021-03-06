# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e2074', '0006_auto_20170423_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicaldiv',
            name='slug',
            field=models.SlugField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='politicaldiv',
            name='group',
            field=models.CharField(choices=[('1', 'Vdc'), ('2', 'Municipality'), ('3', 'Sub-Metropolitan'), ('4', 'Metropolitan')], max_length=1),
        ),
    ]
