from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField


class pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.nome_completo



class Contato(models.Model):
    nome = models.CharField(default=0, max_length=256, blank=True)
    pessoa = models.ForeignKey(pessoa, related_name='contatos',on_delete=models.CASCADE)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    filiacao = models.CharField(max_length=256)
    estado_civil = models.CharField(max_length=256)
    rg = models.IntegerField(null=False)
    cpf = models.IntegerField(null=False)
    endereco = models.CharField(max_length=256)
    numero_de_filhos_menores_de_15 = models.CharField(blank=True, max_length=256)
    idade_1 = models.CharField(max_length=256, blank=True)
    quantos_familiares_trabalham = models.IntegerField(blank=True)
    renda_mensal = models.IntegerField(blank=True)
    atividade_diaadia = models.CharField(max_length=256, null=False)
    dependem_renda = models.IntegerField(blank=True)
    total_renda = models.IntegerField(blank=True)
    bolsa_familia = models.BooleanField(default=False)
    qual_bolsa = models.CharField(max_length=256, blank=True)
    imovel_proprio = models.BooleanField(default=False)
    alugado = models.BooleanField(default=False)
    valor_aluguel = models.IntegerField(blank=True)
    pessoas_especiais = models.BooleanField(default=False)
    quem_doente = models.CharField(max_length=256, blank=True)
    idade = models.IntegerField(blank=True)
    qual_doenca = models.CharField(max_length=256, blank=True)
    certidao_trouxe_na_primeira = models.BooleanField(default=False)
    certidao_vai_trazer = models.BooleanField(default=False)
    certidao_trouxe_na_segunda = models.BooleanField(default=False)
    obs = models.CharField(max_length=512, blank=True)
    data_acolhida = models.DateField(null=True)
    responsavel = models.CharField(max_length=256, null=False)
    retornos = models.CharField(max_length=256, blank=True)


    def __str__(self) -> str:
        return self.nome




