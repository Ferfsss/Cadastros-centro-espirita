from django import forms
from .models import pessoa, Contato


class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
        attrs={"type": "date"}
        )
    )


    class Meta:
        model = pessoa
        ##fields = ['nome_completo', 'data_nascimento', 'ativa']
        ##fields = ['__all__']
        fields = '__all__'

class ContatoForm(forms.ModelForm):
    data_acolhida = forms.DateField(
        widget=forms.TextInput(
        attrs={"type": "date"}
        )
    )
    filiacao = forms.CharField(max_length=256, label="Filiação/Nome da Mãe")
    numero_de_filhos_menores_de_15 = forms.CharField(required=False, max_length=256, label="Número de filhos menores de 15 anos")
    idade_1 = forms.CharField(required=False, max_length=256, label="Idades (digite entre '/')")
    quantos_familiares_trabalham = forms.IntegerField(label="Quantos familiares trabalham?")
    atividade_diaadia = forms.CharField(required=False, max_length=256, label="Qual atividade você desenvolve no seu dia a dia?")
    dependem_renda = forms.IntegerField(required=False, label="Quantas pessoas dependem da renda familiar?")
    total_renda = forms.IntegerField(required=False, label="Total Renda Familiar")
    bolsa_familia = forms.BooleanField(required=False, label="Você ou algum membro da sua família são beneficiarios de programas sociais (Bolsa Família, Benefício de Assistencia Social, etc.)?")
    qual_bolsa = forms.CharField(required=False, label="Qual Bolsa?/Valor")
    pessoas_especiais = forms.BooleanField(required=False, label="Tem pessoas especiais na família(cadeirantes, autistas, idosos, surdos, mudos)?")
    quem_doente = forms.CharField(required=False, label="Quem está doente?")
    
    
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']
        fields = '__all__'



