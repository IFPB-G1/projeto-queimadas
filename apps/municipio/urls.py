from django.urls import path
from .views import *

urlpatterns = [
    path('criar/municipio/', MunicipioCreate.as_view(), name='criar_municipio'),
    path('editar/municipio/<int:pk>/', MunicipioUpdate.as_view(), name='editar_municipio'),
    path('deletar/municipio/<int:pkn>/', MunicipioDelete.as_view(), name='deletar_municipio'),
    path('listar/municipios/', MunicipioList.as_view(), name='listar_municipios'),
    path('detalhar/municipio/<int:pk>/', MunicipioDetail.as_view(), name='detalhar_municipio'),
]