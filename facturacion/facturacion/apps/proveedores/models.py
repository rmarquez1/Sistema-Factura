from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, verbose_name= "Nombre")
    
    def __unicode__(self):
        return self.nombre
    
# Create your models here.
class Factura(models.Model):
	numero = models.IntegerField(primary_key=True)
	fecha_factura = models.DateTimeField()
	monto = models.FloatField()

class Cheque(models.Model):
	numero = models.IntegerField(primary_key=True)
	fecha_cheque = models.DateTimeField()
	monto = models.FloatField()

	
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
	numero_factura = models.ForeignKey(Factura)
	numero_cheque = models.ForeignKey(Cheque)
        base_imponible = models.FloatField()
        iva_doce = models.FloatField()
        monto_factura_entrantes = models.FloatField()
        monto_factura_pagadas = models.FloatField()
	total_factura = models.FloatField()
        iva = models.FloatField()
        cheque_pagar = models.FloatField()