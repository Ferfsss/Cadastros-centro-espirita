from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import  pessoa, Contato
from .forms import PessoaForm, ContatoForm
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render


class ListaPessoaView(ListView):
    model = pessoa
    queryset = pessoa.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
            
        return queryset
    

class PessoaCreateView(CreateView):
    model = pessoa
    form_class = PessoaForm
    success_url = '/pessoas'

class PessoaUpdateView(UpdateView):
    model = pessoa
    form_class = PessoaForm
    success_url = '/pessoas'

class PessoaDeleteView(DeleteView):
    model = pessoa
    success_url = '/pessoas'











def contatos(request, pk_pessoa):
    contatos = Contato.objects.filter(pessoa=pk_pessoa)
    return render(request, 'contato/contato_list.html', {'contatos': contatos, 'pk_pessoa': pk_pessoa})


def contato_novo(request, pk_pessoa):
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.pessoa_id = pk_pessoa;
            contato.save()
            return redirect(reverse('pessoa.contato', args=[pk_pessoa]))

    return render(request, 'contato/contato_form.html', {'form': form})


def contato_editar(request, pk_pessoa, pk):
    contatos = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(instance=contatos)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contatos)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa.contato', args=[pk_pessoa]))

    return render(request, 'contato/contato_form.html', {'form': form})


def contato_remover(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk)
    contato.delete()
    return redirect(reverse('pessoa.contato', args=[pk_pessoa]))
