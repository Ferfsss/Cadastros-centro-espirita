from audioop import reverse
from datetime import datetime
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import doacoes
from .forms import DoacoesForm

class DoacoesView(ListView):
    model = doacoes
    queryset = doacoes.objects.all().order_by('nome_doacao')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_doacao__contains=filtro_nome)
            
        return queryset
    

class DoacoesCreateView(CreateView):
    model = doacoes
    form_class = DoacoesForm
    success_url = 'http://127.0.0.1:8000/doacoes'

class DoacoesUpdateView(UpdateView):
    model = doacoes
    form_class = DoacoesForm
    success_url = 'http://127.0.0.1:8000/doacoes'

class DoacoesDeleteView(DeleteView):
    model = doacoes
    success_url = 'http://127.0.0.1:8000/doacoes' 