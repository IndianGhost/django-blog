# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171009_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='nom',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]