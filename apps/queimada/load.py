import os
from django.contrib.gis.utils import LayerMapping
from .models import Queimada



# Auto-generated `LayerMapping` dictionary for Queimada model
queimada_mapping = {
    'latitude': 'latitude',
    'longitude': 'longitude',
    'brightness': 'brightness',
    'scan': 'scan',
    'track': 'track',
    'acq_date': 'acq_date',
    'acq_time': 'acq_time',
    'satellite': 'satellite',
    'instrument': 'instrument',
    'confidence': 'confidence',
    'version': 'version',
    'bright_t31': 'bright_t31',
    'frp': 'frp',
    'daynight': 'daynight',
    'type': 'type',
    'altitude': 'Altitude e',
    'geom': 'POINT',
}

shp = os.path.abspath(os.path.join('data', 'queimadas_d.shp'))

def run_queimada(verbose=True):
    lm = LayerMapping(Queimada, shp, queimada_mapping)
    lm.save(strict=True, verbose=True)