import datetime 
 
from django.template.loader import get_template 
from django.template import Context 
from django.http import HttpResponse 
 
def fecha_actual(request): 
    ahora = datetime.datetime.now() 
    t = get_template('fecha_actual.html') 
    html = t.render(Context({'fecha_actual': ahora})) 
    return HttpResponse(html) 