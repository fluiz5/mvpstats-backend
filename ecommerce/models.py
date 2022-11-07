
from django.db import models

# Create your models here.
class Jogador (models.Model):
  nome = models.CharField("Nome", max_length=100)
  email = models.CharField("E-mail", max_length=100)
  telefone = models.CharField("Telefone", max_length=100)
  categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, verbose_name="Categoria",null = True)
  posicao = models.CharField("Posição", max_length=100)
  time = models.ForeignKey('Time', on_delete=models.PROTECT, verbose_name="Time")
  def __str__(self):
      return f"{self.nome} - {self.categoria} - {self.time}"
  class Meta:
      verbose_name = "Jogador"
      verbose_name_plural = "Jogadores"

class Campeonato (models.Model):
  nome = models.CharField("Nome", max_length=100)
  categoria = models.CharField("Categoria", max_length=100)
  idade = models.IntegerField()
  times = models.ManyToManyField("Time", verbose_name="Times")
  def __str__(self):
      return f"{self.nome}"
  class Meta:
      verbose_name = "Campeonato"
      verbose_name_plural = "Campeonatos"

  @property
  def partidas(self):
    return Partida.objects.filter(campeonato=self)    

class Time (models.Model):
  nome = models.CharField("Nome", max_length=100)
  tecnico = models.CharField("Técnico", max_length=100)
  def __str__(self):
      return f"{self.nome}"

class Categoria (models.Model):
  idade = models.IntegerField()
  sexo = models.CharField("Sexo", max_length=100)
  def __str__(self):
      return f"{self.sexo} - {self.idade}"  
  
class Estatistica (models.Model):
  ponto = models.IntegerField()
  assistencia = models.IntegerField()
  rebote = models.IntegerField()
  turnover = models.IntegerField()
  tempo = models.IntegerField()
  faltas = models.IntegerField()
  jogador = models.ForeignKey('Jogador', on_delete=models.PROTECT, verbose_name="Jogador")
  partida = models.ForeignKey('Partida', on_delete=models.PROTECT, verbose_name="Partida")

class Partida (models.Model):
  data = models.DateTimeField("Data")
  timeA = models.ForeignKey('Time', on_delete=models.PROTECT, verbose_name="Time A", related_name='timeA')
  pontostimeA = models.IntegerField("Pontos time A", null = True, blank = True)
  timeB = models.ForeignKey('Time', on_delete=models.PROTECT, verbose_name="Time B", related_name='timeB')
  campeonato = models.ForeignKey('Campeonato', on_delete=models.PROTECT, verbose_name="Campeonato")
  pontostimeB = models.IntegerField("Pontos time B", null = True, blank = True)
