from django.urls import path
from .views import ListaAnimalView, AnimalCreateView, AnimalUpdateView, AnimalDeleteView

urlpatterns = [
    path('', ListaAnimalView.as_view(), name='animal.index'),
    path('novo/', AnimalCreateView.as_view(), name='animal.novo'),
    path('editar/<int:pk>', AnimalUpdateView.as_view(), name='animal.editar'),
    path('excluir/<int:pk>', AnimalDeleteView.as_view(), name='animal.excluir'),
]