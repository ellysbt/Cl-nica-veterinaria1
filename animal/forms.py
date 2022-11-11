from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    data_de_nascimento_pet = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Animal
        fields = ['nome_pet', 'data_de_nascimento_pet', 'especie_pet', 'raca_pet']