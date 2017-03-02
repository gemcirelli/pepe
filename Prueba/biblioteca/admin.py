from django.contrib import admin 
from biblioteca.models import Editor, Autor, Libro 
 
admin.site.register(Editor) 
admin.site.register(Autor) 
class LibroAdmin(admin.ModelAdmin): 
    list_display = ('titulo', 'editor', 'fecha_publicacion') 
    list_filter = ('fecha_publicacion',) 
    date_hierarchy = 'fecha_publicacion' 
    ordering = ('titulo',) 
    filter_horizontal = ('autores',) 

admin.site.register(Libro,LibroAdmin)    