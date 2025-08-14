from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_numero, name='cadastro_numero'),  # vazio, para funcionar direto em /cadastro/
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
]
