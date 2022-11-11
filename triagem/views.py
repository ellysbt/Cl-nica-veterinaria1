from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Triagem
from .forms import TriagemForm

class ListaTriagemView(ListView):
    model = Triagem
    queryset = Triagem.objects.all().order_by('nome_do_pet')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_do_pet__contains=filtro_nome)
        return queryset

class TriagemCreateView(CreateView):
    model = Triagem
    form_class = TriagemForm
    success_url = '/triagens'

class TriagemUpdateView(UpdateView):
    model = Triagem
    form_class = TriagemForm
    success_url = '/triagens'

class TriagemDeleteView(DeleteView):
    model = Triagem
    success_url = '/triagens'