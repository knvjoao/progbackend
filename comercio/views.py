from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProdutoForm

def produto_novo(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto registrado no sistema.')
            return redirect('comercio:produto_novo')
    else:
        form = ProdutoForm()
    
    return render(request, 'comercio/produto_form.html', {'form': form})