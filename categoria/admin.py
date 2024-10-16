from django.contrib import admin
from .models import Categoria
from producto.models import Producto


class ProductoInline(admin.TabularInline):
    model= Producto
    extra= 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'descripcion')
    search_fields=('nombre',)
    list_filter=('nombre',)
    ordering=('nombre',)
    #readonly_fields=('nombre',)
    fields=('nombre', 'descripcion')
    inlines= [ProductoInline]
    
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['nombre']
        return super().get_readonly_fields(request, obj)

# Register your models.models here.
admin.site.register(Categoria, CategoriaAdmin)