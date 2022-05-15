from django.contrib import admin
from .models import Queimada
from leaflet.admin import LeafletGeoAdmin

class QueimadaAdmin(LeafletGeoAdmin):
    list_display = ['acq_date', 'acq_time', 'latitude', 'longitude',]
    search_fields = ['acq_date', ]
    list_filter = ['acq_date', 'daynight', 'type',]

admin.site.register(Queimada, QueimadaAdmin)
