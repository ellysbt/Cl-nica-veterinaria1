from django.urls import path
from .views import ListaTriagemView, TriagemCreateView, TriagemUpdateView, TriagemDeleteView

urlpatterns = [
    path('', ListaTriagemView.as_view(), name='triagem.index'),
    path('novo/', TriagemCreateView.as_view(), name='triagem.novo'),
    path('editar/<int:pk>', TriagemUpdateView.as_view(), name='triagem.editar'),
    path('excluir/<int:pk>', TriagemDeleteView.as_view(), name='triagem.excluir'),
]