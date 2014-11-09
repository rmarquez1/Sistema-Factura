
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from facturacion.apps.participante.models import Participante
from facturacion.apps.participante.forms import ParticipanteForm

def inicio(request):
	return render_to_response('inicio/inicio.html', context_instance= RequestContext(request))

def ingresar(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
                        p = Participante.objects.filter(username=usuario, password=clave)
                        if len(p)!=0:
                            return HttpResponseRedirect('/privado/participante')
                        else:
                            return HttpResponse("Este usuario no existe")
	else:
		formulario = AuthenticationForm()
	return render_to_response('inicio/ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))
    
@login_required(login_url='/ingresar')
def privado_participante(request):
    usuario = request.user
    return render_to_response('inicio/inicio_participante.html', {'usuario':usuario}, context_instance=RequestContext(request))