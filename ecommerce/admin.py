from django.contrib import admin

# Register your models here.

from .models import Jogador
from .models import Campeonato
from .models import Time
from .models import Estatistica
from .models import Categoria
from .models import Partida

admin.site.register(Jogador)
admin.site.register(Campeonato)
admin.site.register(Time)
admin.site.register(Estatistica)
admin.site.register(Categoria)
admin.site.register(Partida)