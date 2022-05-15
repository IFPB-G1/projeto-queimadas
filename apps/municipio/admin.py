from django.contrib import admin
from .models import Municipio
from leaflet.admin import LeafletGeoAdmin

class MunicipioAdmin(LeafletGeoAdmin):
    list_display = ['nm_mun', 'cd_mun', ]
    search_fields = ['nm_mun', 'cd_mun', ]

admin.site.register(Municipio, MunicipioAdmin)
