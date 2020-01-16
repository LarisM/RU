from django.contrib import admin

from .models import Funcionario
from .models import Consumidor
from .models import Gru
from .models import Transacao

admin.site.register(Funcionario)
admin.site.register(Consumidor)
admin.site.register(Gru)
admin.site.register(Transacao)