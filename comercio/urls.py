from django.urls import path
from . import views

app_name = "comercio"

urlpatterns = [
    path('produto/novo/', views.produto_novo, name='produto_novo'),
]