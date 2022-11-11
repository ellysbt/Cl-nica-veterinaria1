from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('funcionarios/', include('funcionario.urls')),
    path('animais/', include('animal.urls')),
    path('equipamentos/', include('equipamento.urls')),
    path('clientes/', include('cliente.urls')),
    path('triagens/', include('triagem.urls')),
]