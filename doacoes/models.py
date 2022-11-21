from django.db import models
from pessoa.models import pessoa


class doacoes(models.Model):
    nome_doacao = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)
    rg_ou_cpf = models.CharField(max_length=20)
    telefone = models.IntegerField()
    roupas = models.BooleanField(default=False)
    calcados = models.BooleanField(default=False)
    alimentos = models.BooleanField(default=False)
    material_escolar = models.BooleanField(default=False)
    bebe_mulher = models.BooleanField(default=False)
    bebe_homem = models.BooleanField(default=False)
    idade_bebe = models.CharField(max_length=256)
    numero_bebe = models.IntegerField(null=True)
    numero_calc_bebe = models.IntegerField(null=True)
    obs_bebe = models.CharField(max_length=512, blank=True)
    infant_mulher = models.BooleanField(default=False, null=True)
    quantidade_infant_mulher = models.IntegerField(default=False, null=True)
    idades_mulher = models.CharField(max_length=256, null=True)
    numero_mulher = models.IntegerField(null=True)
    calc_numero_mulher = models.IntegerField(null=True)
    infant_homem = models.BooleanField(default=False, blank=True)
    quantidade_infant_homem = models.IntegerField(null=True)
    idades_homem = models.CharField(max_length=256, blank=True)
    numero_homem = models.IntegerField(null=True)
    calc_numero_homem = models.IntegerField(null=True)
    obs = models.CharField(max_length=512, null=True)
    entregas_realizadas = models.CharField(max_length=4096, null=True)

    def __str__(self) -> str:
        return self.nome_doacao