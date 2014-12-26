#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .forms import ProveedorForm, Resumen_por_proveedorForm, Resumen_proveedoresForm, FacturaForm, ChequeForm
from .models import Resumen_proveedores, Resumen_por_proveedor, Proveedor, Factura, Cheque

def crear_proveedores(request):
    if request.method == 'POST':
	formulario = ProveedorForm(request.POST)
	if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/proveedores/create')
    else:
        formulario = ProveedorForm()
    return render_to_response('proveedores/crear_proveedores.html', {'formulario':formulario}, context_instance= RequestContext(request))

def crear_factura(request):
    if request.method == 'POST':
        formulario = FacturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/proveedores/create_factura')
    else:
        formulario = FacturaForm()
    return render_to_response('proveedores/crear_factura.html', {'formulario':formulario}, context_instance= RequestContext(request))

def crear_cheque(request):
    if request.method == 'POST':
        formulario = ChequeForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/proveedores/create_cheque')
    else:
        formulario = ChequeForm()
    return render_to_response('proveedores/crear_cheque.html', {'formulario':formulario}, context_instance= RequestContext(request))

def resumen_proveedores(request):
    if request.method == 'POST':
        formulario = Resumen_proveedoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/proveedores/resumen_proveedores')
    else:
        formulario = Resumen_proveedoresForm()
    return render_to_response('proveedores/resumen_proveedores.html', {'formulario':formulario}, context_instance=RequestContext(request))

def resumen_por_proveedor(request):
    if request.method == 'POST':
        formulario = Resumen_por_proveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/proveedores/resumen_proveedores')
    else:
        formulario = Resumen_por_proveedorForm()
    return render_to_response('proveedores/resumen_por_proveedor.html', {'formulario':formulario}, context_instance=RequestContext(request))