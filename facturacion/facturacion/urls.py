from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
import settings
urlpatterns = patterns('',
    
    url(r'^', include('facturacion.apps.inicio.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^proveedores/', include('facturacion.apps.proveedores.urls'))
)

urlpatterns += patterns('',
    (r'^imagenes/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)
