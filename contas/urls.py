from django.urls import path
from . import views
urlpatterns = [
    path('' , views.logar , name='logar'),
    path('Criar_conta' , views.Novo_user , name='Novo_user'),
]