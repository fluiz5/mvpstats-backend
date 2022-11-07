from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from ecommerce.models import Time
from ecommerce.models import Jogador
from ecommerce.models import Campeonato
from ecommerce.models import Categoria
from ecommerce.models import Partida
from ecommerce.models import Estatistica


#### Time ########################################
class TimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Time
    fields = ['id', 'nome', 'tecnico']

class TimeViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Time.objects.all().order_by('nome')
  serializer_class = TimeSerializer 
  def get_queryset(self):

    queryset = Time.objects.all().order_by('nome')
    query = {}

    nome = self.request.query_params.get('nome', None)
    if nome is not None:
      query['nome'] = nome
    

    print(query)
    queryset = queryset.filter(**query)    
    return queryset   
######################################################

#### Jogador ########################################
class JogadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Jogador
    fields = ['id', 'nome', 'email', 'telefone', 'categoria', 'posicao', 'time']
    
class JogadorViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Jogador.objects.all().order_by('nome')
  serializer_class = JogadorSerializer
  def get_queryset(self):
    """
    Filtra filme por titulo e ator
    """
    queryset = Jogador.objects.all().order_by('nome')
    query = {}

    nome = self.request.query_params.get('nome', None)
    if nome is not None:
      query['nome'] = nome

    print(query)
    queryset = queryset.filter(**query)    
    return queryset  
###################################################### 



#### Categoria ########################################
class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ['id', 'sexo', 'idade']
    
class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
  serializer_class = CategoriaSerializer
  queryset = Categoria.objects.all().order_by('id')
###################################################### 

#### Partida ########################################
class PartidaSerializer(serializers.ModelSerializer):
  timeA = TimeSerializer()
  timeB = TimeSerializer()
#  campeonato = CampeonatoSerializer()
  class Meta:
    model = Partida
    fields = ['id', 'data', 'timeA', 'pontostimeA', 'timeB', 'pontostimeB']
    
class PartidaViewSet(viewsets.ReadOnlyModelViewSet):
  serializer_class = PartidaSerializer
  queryset = Partida.objects.all().order_by('data')
###################################################### 

#### Campeonato ########################################
class CampeonatoSerializer(serializers.ModelSerializer):
  times = TimeSerializer(many=True, read_only=True)
  partidas = PartidaSerializer(many=True, read_only=True)
  class Meta:
    model = Campeonato
    fields = ['id', 'nome', 'categoria', 'times', 'idade','partidas']
    
class CampeonatoViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Campeonato.objects.all().order_by('nome')
  serializer_class = CampeonatoSerializer
######################################################  

#### Estatística ########################################
class EstatisticaSerializer(serializers.ModelSerializer):
  partida = PartidaSerializer()
  jogador = JogadorSerializer()
  class Meta:
    model = Estatistica
    fields = ['id', 'ponto', 'assistencia', 'rebote', 'turnover', 'tempo', 'faltas', 'jogador', 'partida']
    
class EstatisticaViewSet(viewsets.ReadOnlyModelViewSet):
  serializer_class = EstatisticaSerializer
  queryset = Estatistica.objects.all().order_by('id')
###################################################### 

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'times', TimeViewSet)
router.register(r'jogadores', JogadorViewSet)
router.register(r'campeonatos', CampeonatoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'partida', PartidaViewSet)
router.register(r'estatistica', EstatisticaViewSet)