# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-16 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='esaccesori',
            field=models.BooleanField(default=False),
        ),
    ]