from django.contrib import admin
from .models import Cargo, Trabajador
# Register your models here.




class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','responsabilidades','salario']



class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento','correo', 'get_cargo')

    def get_cargo(self, obj):
        return obj.cargo.nombre if obj.cargo else None

    get_cargo.short_description = 'Cargo'



admin.site.register(Cargo, CargoAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)