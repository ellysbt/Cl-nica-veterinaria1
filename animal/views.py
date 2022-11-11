from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import AnimalForm

class ListaAnimalView(ListView):
    model = Animal
    queryset = Animal.objects.all().order_by('nome_pet')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_pet__contains=filtro_nome)
        return queryset

class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = '/animais'

class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    success_url = '/animais'

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = '/animais'