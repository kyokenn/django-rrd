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
    def handle(self, *args, **options):
        if not args or len(args) < 2:
            print('Usage: ./manage.py rrd_poller <rrd_name> <arg1> [arg2] [arg3] ...')
        else:
            try:
                rrd = RRD.objects.get(name=args[0])
                rrd.update(args[1:])
                print('Done')
            except RRD.DoesNotExist:
                print('RRD with name "%s" does not exists' % args[0])
