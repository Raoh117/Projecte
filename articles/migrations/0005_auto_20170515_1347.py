# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20170511_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carro',
            name='usuari',
        ),
        migrations.RemoveField(
            model_name='comanda',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comanda',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='article',
            name='id_article',
        ),
        migrations.AddField(
            model_name='article',
            name='esconsola',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='carro',
        ),
        migrations.DeleteModel(
            name='comanda',
        ),
    ]