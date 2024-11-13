from django.views.generic import ListView
from .models import Aluno, Curso

#usando genericview

class AlunoListView(ListView):
    model = Aluno
    template_name = 'faculdade/lista_alunos.html'
    context_object_name = 'alunos'

class CursoListView(ListView):
    model = Curso
    template_name = 'faculdade/lista_cursos.html'
    context_object_name = 'cursos'