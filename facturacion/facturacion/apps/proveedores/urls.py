from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^create/$', 'facturacion.apps.proveedores.views.crear_proveedores'),
    url(r'^create_factura/$', 'facturacion.apps.proveedores.views.crear_factura'),
    url(r'^create_cheque/$', 'facturacion.apps.proveedores.views.crear_cheque'),   
)
