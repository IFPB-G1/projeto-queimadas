import os
from django.contrib.gis.utils import LayerMapping
from .models import Municipio

# Auto-generated `LayerMapping` dictionary for Municipio model
municipio_mapping = {
    'cd_mun': 'CD_MUN',
    'nm_mun': 'NM_MUN',
    'sigla': 'SIGLA',
    'area_km2': 'AREA_KM2',
    'geom': 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join('data', 'PB_Municipios_2021.shp'))

def run_municipio(verbose=True):
    lm = LayerMapping(Municipio, shp, municipio_mapping)
    lm.save(strict=True, verbose=True)