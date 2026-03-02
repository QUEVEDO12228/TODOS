from django import forms
from .models import Producto

#formulario de Django
class ProductoForm(forms.ModelForm):
    #configuración del formulario
    class Meta:
        #modelo producto
        model = Producto
        #se utilizan todos los campos del modelo
        fields = '__all__'

        #personalización de los campos del formulario
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),

            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'precio': forms.NumberInput(attrs={'class': 'form-control'}),

            'stock': forms.NumberInput(attrs={'class': 'form-control'}),

            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
