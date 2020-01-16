from django.db import models
from django.contrib.auth.models import User


class Consumidor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    credito = models.FloatField(default=0)
    bolsista = models.BooleanField(default=False)


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=20)


class Gru(models.Model):
    codigo_barras = models.CharField(max_length=30)
    valor = models.FloatField(default=0)
    nome_comprador = models.ForeignKey(Consumidor, null=True, on_delete=models.SET_NULL)
    competencia = models.CharField(max_length=5)
    funcionario = models.ForeignKey(Funcionario, null=True, on_delete=models.SET_NULL)


class Transacao(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    data = models.DateTimeField(auto_now_add=True)
