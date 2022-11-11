from django.urls import path
from .views import ListaFuncionarioView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView

urlpatterns = [
    path('', ListaFuncionarioView.as_view(), name='funcionario.index'),
    path('novo/', FuncionarioCreateView.as_view(), name='funcionario.novo'),
    path('editar/<int:pk>', FuncionarioUpdateView.as_view(), name='funcionario.editar'),
    path('excluir/<int:pk>', FuncionarioDeleteView.as_view(), name='funcionario.excluir'),
]