from django import forms

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
            'imagen'
        ]
        labels = {
            'nombre' : 'Nombre',
            'sexo' : 'Sexo',
            'edad_aproximada' : 'Edad aproximada',
            'fecha_rescate' : 'Fecha rescate',
            'persona' : 'Persona',
            'vacuna' : 'Vacuna',
            'imagen' : 'Imagen'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }