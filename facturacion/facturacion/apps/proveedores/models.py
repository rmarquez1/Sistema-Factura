from django.db import models
from datetime import datetime    

class Proveedor(models.Model):
    nombre = models.CharField(primary_key=True, max_length=200, verbose_name= "Nombre")
    
    def __unicode__(self):
        return self.nombre
    
# Create your models here.
class Factura(models.Model):
	numero = models.IntegerField(primary_key=True)
	monto = models.FloatField(default=0.00)
    
        def __unicode__(self):
            return str(self.numero)

class Cheque(models.Model):
	numero = models.IntegerField(primary_key=True)
	monto = models.FloatField(default=0.00)
        
        def __unicode__(self):
            return str(self.numero)

	
class Resumen_proveedores(models.Model):
        pendiente = 'PD'
        realizado = 'RE'
	nombre = models.ForeignKey(Proveedor)
	monto_bsf = models.FloatField()
	cheque_elaborar = models.FloatField()
	quedaria_en = models.FloatField()
        PENDIENTE_CHOICES = (
            (pendiente, 'Pendiente'),
            (realizado, 'Realizado'),
        )
        pendiente_choices = models.CharField(max_length = 2,
                                            choices = PENDIENTE_CHOICES)

class Resumen_por_proveedor(models.Model):
	nombre = models.ForeignKey(Proveedor)
	numero_factura = models.IntegerField(default=0)
	numero_cheque = models.IntegerField(default=0)
	fecha= models.DateField('%m/%d/%Y')
	base_imponible = models.FloatField(default=0.00)
	iva_doce = models.FloatField(default= 0.00)
	monto_factura_entrantes = models.FloatField(default=0.00)
	monto_factura_pagadas = models.FloatField(default=0.00)
	total_factura = models.FloatField(default = 0.00)
	iva = models.FloatField(default= 0.00)
	cheque_pagar = models.FloatField(default= 0.00)
	
	def __str__(self):
	    return self.numero_factura
        
