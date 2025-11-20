from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro , name='introducao'),
    path('home/', views.home , name='home'),
    path('add/', views.add_aluno , name='add'),
    path('detalhe_aluno/<int:aluno_id>', views.detalhe_aluno, name='detalhe_aluno'),
    path('Excluir/<int:aluno_id>',views.Excluir, name='Excluir' )
    ]