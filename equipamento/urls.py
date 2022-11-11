from django.urls import path
from .views import ListaEquipamentoView, EquipamentoCreateView, EquipamentoUpdateView, EquipamentoDeleteView

urlpatterns = [
    path('', ListaEquipamentoView.as_view(), name='equipamento.index'),
    path('novo/', EquipamentoCreateView.as_view(), name='equipamento.novo'),
    path('editar/<int:pk>', EquipamentoUpdateView.as_view(), name='equipamento.editar'),
    path('excluir/<int:pk>', EquipamentoDeleteView.as_view(), name='equipamento.excluir'),
]