# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='\u6392\u53f7')),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('has_treated', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u786e\u5b9a\u6cbb\u7597')),
            ],
            options={
                'verbose_name': '\u5b89\u6392\u8868',
                'verbose_name_plural': '\u5b89\u6392\u8868',
            },
        ),
    ]
