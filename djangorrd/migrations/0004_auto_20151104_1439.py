# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangorrd', '0003_auto_20151010_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='background_color',
            field=models.CharField(default='dddddd', max_length=6, verbose_name='Background Color #'),
        ),
        migrations.AddField(
            model_name='graph',
            name='canvas_color',
            field=models.CharField(default='ffffff', max_length=6, verbose_name='Canvas Color #'),
        ),
        migrations.AlterField(
            model_name='graph',
            name='color',
            field=models.CharField(default='ff0000', max_length=6, verbose_name='Color #'),
        ),
    ]
