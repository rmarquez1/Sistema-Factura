from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'facturacion.apps.inicio.views.inicio'),
	url(r'^ingresar/$', 'facturacion.apps.inicio.views.ingresar'),
        url(r'^privado/participante$', 'facturacion.apps.inicio.views.privado_participante')
)
	