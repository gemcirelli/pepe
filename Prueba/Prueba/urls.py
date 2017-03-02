
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from Prueba.views import fecha_actual, horas_adelante
from biblioteca import views
from contactos import views as vistacontacto

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante), 
    url(r'^formulariobuscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar), 
    url(r'^contacto/$', vistacontacto.contactos),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
