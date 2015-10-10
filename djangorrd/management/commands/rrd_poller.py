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

from django.core.management import BaseCommand

from ...models import RRD


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('rrd_name', nargs=1, type=str)
        parser.add_argument('rrdtool_arg', nargs='+', type=str)

    def handle(self, *args, **options):
        if not options['rrd_name'] or not options['rrdtool_arg']:
            print('Usage: ./manage.py rrd_poller <rrd_name> <rrdtool_arg1> [rrdtool_arg2] ...')
        else:
            try:
                rrd_name = options['rrd_name'][0]
                rrd = RRD.objects.get(name=rrd_name)
                rrd.update(options['rrdtool_arg'])
                print('Done')
            except RRD.DoesNotExist:
                print('RRD with name "%s" does not exists' % rrd_name)
