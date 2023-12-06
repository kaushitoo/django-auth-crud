from django import forms
from .models import Trabajador, Cargo




class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Correo'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control form-control-sm','type':'date'}),
            'cargo': forms.Select(attrs={'class': 'form-control form-select'}),

        }



    # Esto es para ver los cargos ya que sin esto aparece (objets(1...), con esto se puede ver mejor que cargo se le asigna al Trabajador mas que nada.)
    def __init__(self, *args, **kwargs):
        super(TrabajadorForm, self).__init__(*args, **kwargs)

        # Esto para nada mas no salga en primer lugar el primer cargo
        cargos_choices = [(None, 'Seleccionar Cargo')] + [(cargo.id, cargo.nombre) for cargo in Cargo.objects.all()]
        self.fields['cargo'].widget.choices = cargos_choices


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del Cargo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows':3, 'placeholder': 'Ingrese una Descripcion  del Cargo', 'width':'50px','height':'50px'}),
            'responsabilidades': forms.Textarea(attrs={'class': 'form-control','rows':3, 'placeholder': 'Ingrese las Responsabilidades que tiene el Cargo'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
        }

