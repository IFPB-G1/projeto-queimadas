# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Queimada(models.Model):
    latitude = models.CharField('Latitude', max_length=10)
    longitude = models.CharField('Longitude', max_length=11)
    brightness = models.CharField('Brilho', max_length=7)
    scan = models.CharField('scan', max_length=5)
    track = models.CharField('Track', max_length=5)
    acq_date = models.DateField('Data ACQ')
    acq_time = models.TimeField('Hora ACQ')
    satellite = models.CharField('Satélite', max_length=2)
    instrument = models.CharField('Instrumento', max_length=6)
    confidence = models.CharField('confiança', max_length=2)
    version = models.CharField('Versão', max_length=2)
    bright_t31 = models.CharField('Bright_t31', max_length=7)
    frp = models.CharField('FRP', max_length=7)
    daynight = models.CharField('Dia Noite', max_length=2)
    type = models.CharField('Tipo', max_length=2)
    altitude = models.FloatField('Altitude')
    geom = models.PointField('Geometria', srid=4326)


