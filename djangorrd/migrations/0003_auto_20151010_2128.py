# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangorrd', '0002_auto_20151010_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='border',
            field=models.IntegerField(default=0, help_text='Border width in pixels', verbose_name='Border'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graph',
            name='full_size_mode',
            field=models.BooleanField(default=False, help_text='If true, the width and height specify the final dimensions of the output image', verbose_name='Full size mode'),
        ),
        migrations.AddField(
            model_name='graph',
            name='lazy',
            field=models.BooleanField(default=False, help_text='Only generate the graph if the current graph is out of date or not existent.', verbose_name='Lazy'),
        ),
        migrations.AddField(
            model_name='graph',
            name='slope_mode',
            field=models.BooleanField(default=False, verbose_name='Slope mode'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='rrd',
            field=models.ForeignKey(to='djangorrd.RRD', verbose_name='RRD', related_name='dss'),
        ),
        migrations.AlterField(
            model_name='rra',
            name='cf',
            field=models.CharField(choices=[('AVERAGE', 'AVERAGE'), ('MINIMUM', 'MINIMUM'), ('MAXIMUM', 'MAXIMUM'), ('LAST', 'LAST')], verbose_name='Consolidation Function (CF)', max_length=32),
        ),
        migrations.AlterField(
            model_name='rra',
            name='rrd',
            field=models.ForeignKey(to='djangorrd.RRD', verbose_name='RRD', related_name='rras'),
        ),
        migrations.AlterField(
            model_name='rra',
            name='step',
            field=models.IntegerField(verbose_name='Steps'),
        ),
        migrations.AlterField(
            model_name='rra',
            name='xff',
            field=models.FloatField(verbose_name='Xfiles Factor (XFF)'),
        ),
    ]
