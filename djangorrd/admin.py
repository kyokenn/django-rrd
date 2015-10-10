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

from django.contrib import admin

from .models import RRD, DataSource, RRA, Graph


def regenerate_rrds(modeladmin, request, queryset):
    for rrd in queryset:
        rrd.create(force=True)
regenerate_rrds.short_description = 'Regenerate RRDs'


class DataSourceAdmin(admin.TabularInline):
    model = DataSource
    extra = 0


class RRAAdmin(admin.TabularInline):
    model = RRA
    extra = 0


class RRDAdmin(admin.ModelAdmin):
    actions = regenerate_rrds,
    fields = 'name', 'start', 'step'
    readonly_fields = '_start_tt',
    list_display = 'name', 'start', '_start_tt', 'step',
    inlines = DataSourceAdmin, RRAAdmin


class GraphAdmin(admin.ModelAdmin):
    list_display = 'name', 'title', 'vertical_label', 'rrd'
    list_filter = 'rrd',


admin.site.register(RRD, RRDAdmin)
admin.site.register(Graph, GraphAdmin)
