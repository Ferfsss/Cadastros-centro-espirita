from django import forms
from doacoes.models import doacoes



class DoacoesForm(forms.ModelForm):
    nome_doacao = forms.CharField(max_length=256, label="Nome")
    endereco = forms.CharField(max_length=256, label="Endereço")
    rg_ou_cpf = forms.CharField(max_length=20, label="RG ou CPF")
    telefone = forms.IntegerField(label="Telefone ou Celular")
    roupas = forms.BooleanField(required= False,label="Roupas")
    calcados = forms.BooleanField(required= False,label="Calçados")
    alimentos = forms.BooleanField(required= False,label="Alimentos")
    material_escolar = forms.BooleanField(required= False,label="Material Escolar")
    bebe_mulher = forms.BooleanField(required= False,label="Bebê Feminino")
    bebe_homem = forms.BooleanField(required= False,label="Bebê Masculino")
    idade_bebe = forms.CharField(required= False, max_length=256, label="Idade do(s) bebe(s)")
    numero_bebe = forms.IntegerField(required=False, label="Número de peças")
    numero_calc_bebe = forms.IntegerField(required=False, label="Número de calçados")
    obs_bebe = forms.CharField(max_length=512, required=False, label="Observações")
    infant_mulher = forms.BooleanField(required=False, label="Infantil feminino")
    quantidade_infant_mulher = forms.IntegerField(required=False, label="Quantidade")
    idades_mulher = forms.CharField(max_length=256, required=False, label="Idade(s), digite entre '/' ")
    numero_mulher = forms.IntegerField(required=False, label="Número de peças")
    calc_numero_mulher = forms.IntegerField(required=False, label="Numero de Calçados")
    infant_homem = forms.BooleanField(required=False, label="Infantil masculino")
    quantidade_infant_homem = forms.IntegerField(required=False, label="Quantidade")
    idades_homem = forms.CharField(required=False, label="Idade(s), digite entre '/' ")
    numero_homem = forms.IntegerField(required=False, label="Número de peças")
    calc_numero_homem = forms.IntegerField(required=False, label="Numero de Calçados")
    obs = forms.CharField(required=False, label="Observações")
    entregas_realizadas = forms.CharField(required=False, label="Observações")

    class Meta:
        model = doacoes
        fields = '__all__'