from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^create/$', 'facturacion.apps.proveedores.views.crear_proveedores'),
    #url(r'^create_factura/$', 'facturacion.apps.proveedores.views.crear_factura'),
    #url(r'^create_cheque/$', 'facturacion.apps.proveedores.views.crear_cheque'),
    url(r'^resumen_proveedores/$', 'facturacion.apps.proveedores.views.resumen_proveedores'),
    url(r'^seleccion_accion/$', 'facturacion.apps.proveedores.views.seleccion_accion'),
    url(r'^accion_factura/$', 'facturacion.apps.proveedores.views.accion_factura'),
    url(r'^seleccion_proveedor/$', 'facturacion.apps.proveedores.views.seleccion_proveedor'),
    url(r'^seleccion_facturas/$', 'facturacion.apps.proveedores.views.seleccion_facturas'),
    url(r'^obtener_facturas/$', 'facturacion.apps.proveedores.views.obtener_facturas'),
    url(r'^seleccion_resumen/$', 'facturacion.apps.proveedores.views.seleccion_resumen'),
    url(r'^resumen_por_proveedor/$', 'facturacion.apps.proveedores.views.resumen_por_proveedor'),
)
