# Copyright (C) 2015 Okami, okami@fuzetsu.info

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import calendar
import datetime
import os
import rrdtool
import time

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


DST = (
    ('COUNTER', 'COUNTER'),
    ('DERIVE', 'DERIVE'),
    ('ABSOLUTE', 'ABSOLUTE'),
    ('GAUGE', 'GAUGE'))

CF = (
    ('AVERAGE', 'AVERAGE'),
    ('MINIMUM', 'MINIMUM'),
    ('MAXIMUM', 'MAXIMUM'),
    ('LAST', 'LAST'))


class RRD(models.Model):
    name = models.TextField('RRD Name', unique=True)
    start = models.DateTimeField(
        'Start time', help_text='Start time (current time by default)',
        blank=True, null=True)
    step = models.IntegerField(
        'Step', help_text='Step in seconds (300 by default)',
        blank=True, null=True)

    def _start_tt(self):
        return int(time.mktime(self.start.timetuple()))
    _start_tt.short_description = 'Start (unix)'

    def get_path(self):
        RRD_DIR = os.path.join(settings.MEDIA_ROOT, 'rrd')
        if not os.path.exists(RRD_DIR):
            os.makedirs(RRD_DIR)
        return os.path.join(RRD_DIR, '%s.rrd' % self.name)

    def rrd_exists(self):
        return os.path.exists(self.get_path())

    def create(self):
        if self.dss.exists() and self.rras.exists():
            dss = tuple(map(lambda ds: ds.get_args(), self.dss.all()))
            rras = tuple(map(lambda rra: rra.get_args(), self.rras.all()))
            args = (
                self.get_path(),
                # '--start', str(int(calendar.timegm(self.start.timetuple()))),
                '--start', str(int(time.mktime(self.start.timetuple()))),
                '--step', str(self.step)) + dss + rras
            rrdtool.create(*args)

    def update(self, args):
        rrdargs = [self.get_path()]
        rrdargs += list(args)
        rrdtool.update(*rrdargs)

    def save(self, **kwargs):
        if not self.start:
            self.start = datetime.datetime.now()
        if not self.step:
            self.step = 300
        super().save(**kwargs)

        if not self.rrd_exists():
            self.create()

    def delete(self, **kwargs):
        super().delete(**kwargs)

        if self.rrd_exists():
            os.remove(self.get_path())

    def get_args(self, color):
        ''' get args for rrdtool graph '''
        defs = tuple(map(
            lambda ds: 'DEF:%s=%s:%s:AVERAGE' % (ds.name, self.get_path(), ds.name),
            self.dss.all()))
        areas = tuple(map(
            lambda ds: 'AREA:%s#%s:%s' % (ds.name, color, ds.name),
            self.dss.all()))
        return defs + areas

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = 'RR Database'
        verbose_name_plural = 'RR Databases'


class DataSource(models.Model):
    rrd = models.ForeignKey(RRD, verbose_name='RRD Database', related_name='dss')
    name = models.CharField('Variable Name', max_length=255)
    dst = models.CharField('Data Source Type', max_length=32, choices=DST)
    # if None then fallback to step*2 from rrd
    heartbeat = models.IntegerField('Heartbeat', blank=True, null=True)
    min = models.IntegerField('Minimum value', blank=True, null=True)
    max = models.IntegerField('Maximum value', blank=True, null=True)

    def get_heartbeat(self):
        return self.heartbeat or (self.rrd.step * 2)

    def get_args(self):
        ''' get args for rrdtool create '''
        return 'DS:%(variable_name)s:%(DST)s:%(heartbeat)s:%(min)s:%(max)s' % {
            'variable_name': self.name,
            'DST': self.dst,
            'heartbeat': self.get_heartbeat(),
            'min': 'U' if self.min is None else self.min,
            'max': 'U' if self.max is None else self.max,
        }

    def __str__(self):
        return self.get_args()

    class Meta(object):
        verbose_name = 'Data Source'
        verbose_name_plural = 'Data Sources'


class RRA(models.Model):
    rrd = models.ForeignKey(RRD, verbose_name='RRD Database', related_name='rras')
    cf = models.CharField('Consolidation Function', max_length=32, choices=CF)
    xff = models.FloatField('XFF')
    step = models.IntegerField('Step')
    rows = models.IntegerField('Rows')

    def get_args(self):
        ''' get args for rrdtool create '''
        return 'RRA:%(CF)s:%(xff)s:%(step)s:%(rows)s' % {
            'CF': self.cf,
            'xff': self.xff,
            'step': self.step,
            'rows': self.rows,
        }

    def __str__(self):
        return self.get_args()

    class Meta(object):
        verbose_name = 'RR Archive'
        verbose_name_plural = 'RR Archives'


class Graph(models.Model):
    rrd = models.ForeignKey(RRD, verbose_name='RRD Database', related_name='graphs')
    name = models.CharField('Name', max_length=255, unique=True)
    title = models.CharField('Title', max_length=255)
    vertical_label = models.CharField('Vertical Label', max_length=255)
    period = models.IntegerField('Period', help_text='Period in seconds')
    color = models.CharField('Color #', max_length=6)
    width = models.IntegerField('Width', help_text='Width in pixels')
    height = models.IntegerField('Height', help_text='Height in pixels')

    def get_path(self):
        RRD_DIR = os.path.join(settings.MEDIA_ROOT, 'rrd')
        if not os.path.exists(RRD_DIR):
            os.makedirs(RRD_DIR)
        return os.path.join(RRD_DIR, '%s.png' % self.pk)

    def graph(self):
        # t = int(calendar.timegm(datetime.datetime.now().timetuple()))
        t = int(time.mktime(datetime.datetime.now().timetuple()))
        args = (
            self.get_path(),
            '--title', self.title,
            '--vertical-label', self.vertical_label,
            '--imgformat', 'PNG',
            '--width', str(self.width), '--height', str(self.height),
            '--start', str(int(t - self.period / 2)),
            '--end', str(int(t + self.period / 2)),
        ) + self.rrd.get_args(self.color)
        rrdtool.graph(*args)

    def get_absolute_url(self):
        return reverse('rrd:graph', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'RR Graph'
        verbose_name_plural = 'RR Graphs'
