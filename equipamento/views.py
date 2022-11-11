from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Equipamento
from .forms import EquipamentoForm

class ListaEquipamentoView(ListView):
    model = Equipamento
    queryset = Equipamento.objects.all().order_by('nome_equipamento')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_equipamento__contains=filtro_nome)
        return queryset

class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    success_url = '/equipamentos'

class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    success_url = '/equipamentos'

class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    success_url = '/equipamentos'