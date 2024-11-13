from django.urls import path
from .views import AlunoListView, CursoListView

#incluindo app name para caso de conflitos em nomes de file. ao referenciar links, usar app name com nome da file

app_name = 'faculdade'

urlpatterns = [
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('cursos/', CursoListView.as_view(), name='curso-list'),
]