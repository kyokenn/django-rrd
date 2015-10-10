# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorrd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rrd',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start time', help_text='Start time (current time by default)'),
        ),
        migrations.AlterField(
            model_name='rrd',
            name='step',
            field=models.IntegerField(blank=True, null=True, verbose_name='Step', help_text='Step in seconds (300 by default)'),
        ),
    ]
