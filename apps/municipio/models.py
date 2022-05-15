# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Municipio(models.Model):
    cd_mun = models.CharField('Código do município', max_length=7)
    nm_mun = models.CharField('Nome do município', max_length=60)
    sigla = models.CharField('Sigla', max_length=2)
    area_km2 = models.FloatField('Área em Km2')
    geom = models.MultiPolygonField('Geometria', srid=4674)

    def __str__(self):
        return self.nm_mun
