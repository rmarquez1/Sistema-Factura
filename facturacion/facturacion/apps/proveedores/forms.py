from django import forms
from .models import Resumen_proveedores, Resumen_por_proveedor, Proveedor, Factura, Cheque

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

class Resumen_proveedoresForm(forms.ModelForm):
	class Meta:
		model = Resumen_proveedores

class Resumen_por_proveedorForm(forms.ModelForm):
	class Meta:
		model = Resumen_por_proveedor


class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura

class ChequeForm(forms.ModelForm):
	class Meta:
		model = Cheque