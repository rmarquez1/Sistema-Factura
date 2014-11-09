from .models import Resumen_proveedores, Resumen_por_proveedor, Proveedor, Factura, Cheque
from django.contrib import admin

admin.site.register(Proveedor)
admin.site.register(Resumen_proveedores)
admin.site.register(Resumen_por_proveedor)
admin.site.register(Factura)
admin.site.register(Cheque)