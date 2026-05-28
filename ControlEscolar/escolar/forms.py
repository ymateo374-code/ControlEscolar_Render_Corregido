from django import forms
from .models import Carrera, Profesor, Estudiante, Materia, Aula, PeriodoSemestral, Horario, Grupo, Calificacion


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = 'form-select' if isinstance(field.widget, (forms.Select, forms.SelectMultiple)) else 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                css = 'form-check-input'
            field.widget.attrs.update({'class': css})


class CarreraForm(BootstrapModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'


class ProfesorForm(BootstrapModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'


class EstudianteForm(BootstrapModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'


class MateriaForm(BootstrapModelForm):
    class Meta:
        model = Materia
        fields = '__all__'


class AulaForm(BootstrapModelForm):
    class Meta:
        model = Aula
        fields = '__all__'


class PeriodoSemestralForm(BootstrapModelForm):
    class Meta:
        model = PeriodoSemestral
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class HorarioForm(BootstrapModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }


class GrupoForm(BootstrapModelForm):
    class Meta:
        model = Grupo
        exclude = ['estudiantes']

class CalificacionForm(BootstrapModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        estudiante = cleaned_data.get('estudiante')
        grupo = cleaned_data.get('grupo')

        if estudiante and grupo and not grupo.estudiantes.filter(pk=estudiante.pk).exists():
            self.add_error(
                'estudiante',
                'Este alumno no pertenece al grupo seleccionado. Primero agrégalo al grupo.'
            )

        return cleaned_data