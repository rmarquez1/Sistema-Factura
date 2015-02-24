#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .forms import ProveedorForm, Resumen_por_proveedorForm, Resumen_proveedoresForm, FacturaForm, ChequeForm, SeleccionFacturasForm
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
"""
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
"""
def resumen_proveedores(request):
    if request.method == 'POST':
        formulario = Resumen_proveedoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/proveedores/resumen_proveedores')
    else:
        formulario = Resumen_proveedoresForm()
    return render_to_response('proveedores/resumen_proveedores.html', {'formulario':formulario}, context_instance=RequestContext(request))

def accion_factura(request):
    if request.method == 'POST':
        #Buscamos el proveedor correspondiete
        nombre = request.POST["nombre"]
        proveedor = Proveedor.objects.filter(nombre=nombre)
        nombre_proveedor = proveedor[0]
        
        fecha = request.POST["fecha"]
        
        #Buscamos la factura correspondiente
        numero_factura = request.POST["numero_factura"]
        base_imponible = request.POST["base_imponible"]
        iva_12 = float(base_imponible) * 0.12
        monto_factura = request.POST["monto_factura_entrantes"]
        iva_75 = iva_12 * 0.75
        cheque_pagar = float(monto_factura) - iva_75
        
        #Creamos la factura
        factura = Factura(numero = numero_factura, monto=monto_factura)
        factura.save()
        
        facturas = Factura.objects.all()
        total_factura = calculo_total_factura(facturas)
        
        # Creacion del resumen
        resumen = Resumen_por_proveedor(    nombre=nombre_proveedor,
                                            fecha=fecha,
                                            numero_factura = numero_factura, 
                                            base_imponible=base_imponible,
                                            iva_doce = iva_12,
                                            monto_factura_entrantes=monto_factura,
                                            total_factura=total_factura,
                                            iva = iva_75,
                                            cheque_pagar=cheque_pagar)
        resumen.save()
        return HttpResponseRedirect('/proveedores/accion_factura')
    else:
        formulario = Resumen_por_proveedorForm()
    return render_to_response('proveedores/accion_factura.html', {'formulario':formulario}, context_instance=RequestContext(request))

def seleccion_accion(request):
    option = request.POST.get('factura')
    if option == 'f':
        return HttpResponseRedirect('/proveedores/accion_factura')
    elif option == 'c':
        return HttpResponseRedirect('/proveedores/accion_cheque')
    return render_to_response('proveedores/seleccion_accion.html',context_instance=RequestContext(request))


def seleccion_resumen(request):
    proveedor = Resumen_por_proveedorForm()
    return render_to_response('proveedores/seleccion_resumen.html',
                              {'proveedor':proveedor},
                              context_instance=RequestContext(request))

def resumen_por_proveedor(request):
    nombre = request.POST["nombre"]
    proveedor = Proveedor.objects.filter(nombre=nombre)
    resumen = Resumen_por_proveedor.objects.filter(nombre=proveedor[0])
    return render_to_response('proveedores/resumen_por_proveedor.html',
                              {'nombre':nombre,'resumen': resumen},
                              context_instance=RequestContext(request))

def seleccion_proveedor(request):
    proveedor = Resumen_por_proveedorForm()
    return render_to_response('proveedores/seleccion_proveedor.html',
                              {'proveedor':proveedor},
                              context_instance=RequestContext(request))

def seleccion_facturas(request):
    nombre = request.POST["nombre"]
    
    proveedor = Proveedor.objects.filter(nombre=nombre)
    formulario = SeleccionFacturasForm()

    formulario.fields['facturas'].choices=[(x.nombre,x.numero_factura,x.numero_cheque,
        x.fecha,x.base_imponible,x.iva_doce,x.monto_factura_entrantes,x.monto_factura_pagadas,
        x.total_factura,x.iva,x.cheque_pagar) for x in Resumen_por_proveedor.objects.filter(nombre=proveedor[0])]

    return render_to_response('proveedores/seleccion_facturas.html',
                              {'formulario':formulario,'nombre':nombre},
                              context_instance=RequestContext(request))

def obtener_facturas(request):
    lista_facturas = request.POST.getlist('facturas')
    print type(lista_facturas[0])

    nombre = 'NOMBRE'
    formulario = SeleccionFacturasForm()
    formulario.fields['facturas'].choices=[(x.nombre,x.numero_factura,x.numero_cheque,
        x.fecha,x.base_imponible,x.iva_doce,x.monto_factura_entrantes,x.monto_factura_pagadas,
        x.total_factura,x.iva,x.cheque_pagar) for x in Resumen_por_proveedor.objects.all()]

    return render_to_response('proveedores/seleccion_facturas.html',
                              {'formulario':formulario,'nombre':nombre},
                              context_instance=RequestContext(request))

'''
def seleccion_facturas(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        print nombre
        proveedor = Proveedor.objects.filter(nombre=nombre)

        print proveedor[0]

        formulario=SeleccionFacturasForm(request.POST)
        lista_facturas_seleccionadas = request.POST.getlist('facturas')

        # Calculando la suma de las facturas seleccionadas
        suma = 0
        for lista in lista_facturas_seleccionadas:
            numero = int(lista)
            suma = Resumen_por_proveedor.objects.filter(nombre=proveedor[0],numero_factura=numero)[0].monto_factura_entrantes
            
        print suma
        
        return HttpResponseRedirect('/proveedores/seleccion_facturas')
    else:
        formulario = SeleccionFacturasForm()
    return render_to_response('proveedores/seleccion_facturas.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))
'''
def calculo_total_factura(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i].monto

    return sum