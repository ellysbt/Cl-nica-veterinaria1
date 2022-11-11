from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = ['nome_do_pet', 'sintomas']