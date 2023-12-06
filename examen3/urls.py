
from django.contrib import admin
from django.urls import path
from tasks import views


urlpatterns = [

    # Inicio
    path('',views.index, name="inicio"),
    path('inicio/',views.index, name="inicio"),


    # Url de Trabajadores
    path('trabajadores/',views.trabajadores_list, name='trabajadores_list'),
    path('actualizarTrabajador/<int:id>', views.actualizar_trabajador, name='actualizar_trabajador'),
    path('eliminarTrabajador/<int:id>', views.eliminarTrabajador, name="eliminar_trabajador"),
    path('agregarTrabajador/', views.agregarTrabajador, name='agregar_trabajador'),



    # Url de Cargos
    path('cargos/',views.cargos_list, name='cargos_list'),
    path('actualizarCargo/<int:id>', views.actualizar_cargo, name='actualizar_cargo'),
    path('eliminarCargo/<int:id>', views.eliminarCargo, name="eliminar_cargo"),
    path('agregarCargo/', views.agregarCargo, name='agregar_cargo'),






    # Url a la base de django
    path('admin/', admin.site.urls),
]
