
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from Prueba.views import fecha_actual, horas_adelante

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante), 
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
