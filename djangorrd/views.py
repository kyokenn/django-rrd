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

import os

from django.http import HttpResponse, Http404
from django.views.generic import DetailView

from wsgiref.util import FileWrapper

from .models import Graph


class GraphView(DetailView):
    queryset = Graph.objects
    slug_field = 'name'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.graph()
        path = self.object.get_path()
        if os.path.exists(path) and os.path.isfile(path):
            wrapper = FileWrapper(open(path, 'rb'))
            response = HttpResponse(wrapper, content_type='image/png')
            response['Content-Length'] = os.path.getsize(path)
            return response
        else:
            raise Http404
