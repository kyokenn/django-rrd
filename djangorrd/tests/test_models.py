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

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from ..models import RRD, DataSource, RRA, Graph


class ModelsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_everything(self):
        rrd = RRD.objects.create(name='test')
        ds = DataSource.objects.create(rrd=rrd, name='x', dst='GAUGE')
        rra = RRA.objects.create(
            rrd=rrd, cf='AVERAGE', xff=0.5, step=1, rows=24)
        graph = Graph.objects.create(
            rrd=rrd, name='test', title='Test Graph', vertical_label='Units',
            period=600, color='ff0000', width=500, height=300, border=2)

        rrd.create(force=True)
        rrd.update(['N:10'])

        response = self.client.get(
            reverse('rrd:graph', kwargs={'slug': graph.name}))
        self.assertEqual(response.status_code, 200)
