from django.shortcuts import render, redirect
from .models import Trabajador, Cargo
from .forms import TrabajadorForm, CargoForm





# Pagina Inicio

def index(request):
    return render(request,"index.html")



# Funciones para tabla Trabajadores

# views.py en tu aplicación tasks


def agregarTrabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/trabajadores')
    else:
        form = TrabajadorForm()

    return render(request, 'agregar_trabajador.html', {'form': form})


def actualizar_trabajador(request, id):
    trabajador = Trabajador.objects.get(id=id)
    form = TrabajadorForm(instance=trabajador)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('/trabajadores')
    data = {'form': form}
    return render(request, 'actualizar_trabajador.html', data)


def eliminarTrabajador(request, id):
    lista = Trabajador.objects.get(id = id)
    lista.delete()
    return redirect('/trabajadores')



def trabajadores_list(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajadores_list.html', {'trabajadores': trabajadores})



# Funciones para la tabla Cargos




def agregarCargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cargos')
    else:
        form = CargoForm()

    return render(request, 'agregar_cargo.html', {'form': form})

def cargos_list(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargos_list.html', {'cargos': cargos})


def eliminarCargo(request, id):
    cargo = Cargo.objects.get(id = id)
    cargo.delete()
    return redirect('/cargos')


def actualizar_cargo(request, id):
    cargo = Cargo.objects.get(id=id)
    form = CargoForm(instance=cargo)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('/cargos')
    data = {'form': form}
    return render(request, 'actualizar_cargo.html', data)




