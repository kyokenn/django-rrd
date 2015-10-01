# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Variable Name', max_length=255)),
                ('dst', models.CharField(verbose_name='Data Source Type', max_length=32, choices=[('COUNTER', 'COUNTER'), ('DERIVE', 'DERIVE'), ('ABSOLUTE', 'ABSOLUTE'), ('GAUGE', 'GAUGE')])),
                ('heartbeat', models.IntegerField(null=True, verbose_name='Heartbeat', blank=True)),
                ('min', models.IntegerField(null=True, verbose_name='Minimum value', blank=True)),
                ('max', models.IntegerField(null=True, verbose_name='Maximum value', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Data Sources',
                'verbose_name': 'Data Source',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=255)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('vertical_label', models.CharField(verbose_name='Vertical Label', max_length=255)),
                ('period', models.IntegerField(verbose_name='Period', help_text='Period in seconds')),
                ('color', models.CharField(verbose_name='Color #', max_length=6)),
                ('width', models.IntegerField(verbose_name='Width', help_text='Width in pixels')),
                ('height', models.IntegerField(verbose_name='Height', help_text='Height in pixels')),
            ],
            options={
                'verbose_name_plural': 'RR Graphs',
                'verbose_name': 'RR Graph',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RRA',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cf', models.CharField(verbose_name='Consolidation Function', max_length=32, choices=[('AVERAGE', 'AVERAGE'), ('MINIMUM', 'MINIMUM'), ('MAXIMUM', 'MAXIMUM'), ('LAST', 'LAST')])),
                ('xff', models.FloatField(verbose_name='XFF')),
                ('step', models.IntegerField(verbose_name='Step')),
                ('rows', models.IntegerField(verbose_name='Rows')),
            ],
            options={
                'verbose_name_plural': 'RR Archives',
                'verbose_name': 'RR Archive',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RRD',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(unique=True, verbose_name='RRD Name')),
                ('start', models.DateTimeField(null=True, verbose_name='Start time', blank=True)),
                ('step', models.IntegerField(verbose_name='Step', help_text='Step in seconds')),
            ],
            options={
                'verbose_name_plural': 'RR Databases',
                'verbose_name': 'RR Database',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rra',
            name='rrd',
            field=models.ForeignKey(related_name='rras', verbose_name='RRD Database', to='djangorrd.RRD'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='graph',
            name='rrd',
            field=models.ForeignKey(related_name='graphs', verbose_name='RRD Database', to='djangorrd.RRD'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasource',
            name='rrd',
            field=models.ForeignKey(related_name='dss', verbose_name='RRD Database', to='djangorrd.RRD'),
            preserve_default=True,
        ),
    ]
