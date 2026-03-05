from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#si no esta logueado lo envia al inicio
@login_required
def inicio(request):
    return render(request, 'core/inicio.html')