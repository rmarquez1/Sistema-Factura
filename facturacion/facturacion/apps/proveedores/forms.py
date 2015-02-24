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
                
        def pertenece_factura(self):
            factura = self.cleaned_data['numero_factura']
            
            facturas = Factura.objects.filter(numero=factura)
            if len(facturas) != 0:
                raise forms.ValidationError("Ya existe este numero de factura")
            return factura


class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura

class ChequeForm(forms.ModelForm):
	class Meta:
		model = Cheque


class SeleccionFacturasForm(forms.Form):
	facturas = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Escoja las facturas")