from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Carrera, Profesor, Estudiante, Materia, Aula, PeriodoSemestral, Horario, Grupo, Calificacion
from django.db.models import Avg
from django.http import HttpResponse
from .forms import CarreraForm, ProfesorForm, EstudianteForm, MateriaForm, AulaForm, PeriodoSemestralForm, HorarioForm, GrupoForm, CalificacionForm


def dashboard(request):
    context = {
        'total_carreras': Carrera.objects.count(),
        'total_profesores': Profesor.objects.count(),
        'total_estudiantes': Estudiante.objects.count(),
        'total_materias': Materia.objects.count(),
        'total_aulas': Aula.objects.count(),
        'total_grupos': Grupo.objects.count(),
        'total_calificaciones': Calificacion.objects.count(),
        'grupos_recientes': Grupo.objects.select_related('materia', 'profesor', 'aula', 'periodo')[:5],
    }
    return render(request, 'escolar/dashboard.html', context)


class BaseListView(ListView):
    template_name = 'escolar/lista.html'
    context_object_name = 'objetos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo': self.titulo,
            'crear_url': self.crear_url,
            'editar_url': self.editar_url,
            'eliminar_url': self.eliminar_url,
            'detalle_url': getattr(self, 'detalle_url', None),
            'columnas': self.columnas,
        })
        return context


class BaseCreateView(CreateView):
    template_name = 'escolar/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f"Registrar {self.titulo}"
        context['volver_url'] = self.success_url_name
        return context


class BaseUpdateView(UpdateView):
    template_name = 'escolar/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f"Editar {self.titulo}"
        context['volver_url'] = self.success_url_name
        return context


class BaseDeleteView(DeleteView):
    template_name = 'escolar/confirmar_eliminar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f"Eliminar {self.titulo}"
        context['volver_url'] = self.success_url_name
        return context


class CarreraListView(BaseListView):
    model = Carrera
    titulo = 'Carreras'
    crear_url = 'carrera_crear'
    editar_url = 'carrera_editar'
    eliminar_url = 'carrera_eliminar'
    columnas = [('clave', 'Clave'), ('nombre', 'Nombre'), ('descripcion', 'Descripción')]


class CarreraCreateView(BaseCreateView):
    model = Carrera
    form_class = CarreraForm
    titulo = 'Carrera'
    success_url = reverse_lazy('carrera_lista')
    success_url_name = 'carrera_lista'


class CarreraUpdateView(BaseUpdateView):
    model = Carrera
    form_class = CarreraForm
    titulo = 'Carrera'
    success_url = reverse_lazy('carrera_lista')
    success_url_name = 'carrera_lista'


class CarreraDeleteView(BaseDeleteView):
    model = Carrera
    titulo = 'Carrera'
    success_url = reverse_lazy('carrera_lista')
    success_url_name = 'carrera_lista'


class ProfesorListView(BaseListView):
    model = Profesor
    titulo = 'Profesores'
    crear_url = 'profesor_crear'
    editar_url = 'profesor_editar'
    eliminar_url = 'profesor_eliminar'
    columnas = [('nombre', 'Nombre'), ('apellido_paterno', 'Apellido'), ('correo', 'Correo'), ('especialidad', 'Especialidad')]


class ProfesorCreateView(BaseCreateView):
    model = Profesor
    form_class = ProfesorForm
    titulo = 'Profesor'
    success_url = reverse_lazy('profesor_lista')
    success_url_name = 'profesor_lista'


class ProfesorUpdateView(BaseUpdateView):
    model = Profesor
    form_class = ProfesorForm
    titulo = 'Profesor'
    success_url = reverse_lazy('profesor_lista')
    success_url_name = 'profesor_lista'


class ProfesorDeleteView(BaseDeleteView):
    model = Profesor
    titulo = 'Profesor'
    success_url = reverse_lazy('profesor_lista')
    success_url_name = 'profesor_lista'


class EstudianteListView(BaseListView):
    model = Estudiante
    titulo = 'Estudiantes'
    crear_url = 'estudiante_crear'
    editar_url = 'estudiante_editar'
    eliminar_url = 'estudiante_eliminar'
    columnas = [('numero_control', 'No. Control'), ('nombre', 'Nombre'), ('apellido_paterno', 'Apellido'), ('carrera', 'Carrera'), ('semestre', 'Semestre')]


class EstudianteCreateView(BaseCreateView):
    model = Estudiante
    form_class = EstudianteForm
    titulo = 'Estudiante'
    success_url = reverse_lazy('estudiante_lista')
    success_url_name = 'estudiante_lista'


class EstudianteUpdateView(BaseUpdateView):
    model = Estudiante
    form_class = EstudianteForm
    titulo = 'Estudiante'
    success_url = reverse_lazy('estudiante_lista')
    success_url_name = 'estudiante_lista'


class EstudianteDeleteView(BaseDeleteView):
    model = Estudiante
    titulo = 'Estudiante'
    success_url = reverse_lazy('estudiante_lista')
    success_url_name = 'estudiante_lista'


class MateriaListView(BaseListView):
    model = Materia
    titulo = 'Materias'
    crear_url = 'materia_crear'
    editar_url = 'materia_editar'
    eliminar_url = 'materia_eliminar'
    columnas = [('clave', 'Clave'), ('nombre', 'Nombre'), ('creditos', 'Créditos'), ('carrera', 'Carrera')]


class MateriaCreateView(BaseCreateView):
    model = Materia
    form_class = MateriaForm
    titulo = 'Materia'
    success_url = reverse_lazy('materia_lista')
    success_url_name = 'materia_lista'


class MateriaUpdateView(BaseUpdateView):
    model = Materia
    form_class = MateriaForm
    titulo = 'Materia'
    success_url = reverse_lazy('materia_lista')
    success_url_name = 'materia_lista'


class MateriaDeleteView(BaseDeleteView):
    model = Materia
    titulo = 'Materia'
    success_url = reverse_lazy('materia_lista')
    success_url_name = 'materia_lista'


class AulaListView(BaseListView):
    model = Aula
    titulo = 'Aulas'
    crear_url = 'aula_crear'
    editar_url = 'aula_editar'
    eliminar_url = 'aula_eliminar'
    columnas = [('nombre', 'Aula'), ('capacidad', 'Capacidad'), ('ubicacion', 'Ubicación')]


class AulaCreateView(BaseCreateView):
    model = Aula
    form_class = AulaForm
    titulo = 'Aula'
    success_url = reverse_lazy('aula_lista')
    success_url_name = 'aula_lista'


class AulaUpdateView(BaseUpdateView):
    model = Aula
    form_class = AulaForm
    titulo = 'Aula'
    success_url = reverse_lazy('aula_lista')
    success_url_name = 'aula_lista'


class AulaDeleteView(BaseDeleteView):
    model = Aula
    titulo = 'Aula'
    success_url = reverse_lazy('aula_lista')
    success_url_name = 'aula_lista'


class PeriodoListView(BaseListView):
    model = PeriodoSemestral
    titulo = 'Periodos Semestrales'
    crear_url = 'periodo_crear'
    editar_url = 'periodo_editar'
    eliminar_url = 'periodo_eliminar'
    columnas = [('nombre', 'Periodo'), ('fecha_inicio', 'Inicio'), ('fecha_fin', 'Fin'), ('activo', 'Activo')]


class PeriodoCreateView(BaseCreateView):
    model = PeriodoSemestral
    form_class = PeriodoSemestralForm
    titulo = 'Periodo'
    success_url = reverse_lazy('periodo_lista')
    success_url_name = 'periodo_lista'


class PeriodoUpdateView(BaseUpdateView):
    model = PeriodoSemestral
    form_class = PeriodoSemestralForm
    titulo = 'Periodo'
    success_url = reverse_lazy('periodo_lista')
    success_url_name = 'periodo_lista'


class PeriodoDeleteView(BaseDeleteView):
    model = PeriodoSemestral
    titulo = 'Periodo'
    success_url = reverse_lazy('periodo_lista')
    success_url_name = 'periodo_lista'


class HorarioListView(BaseListView):
    model = Horario
    titulo = 'Horarios'
    crear_url = 'horario_crear'
    editar_url = 'horario_editar'
    eliminar_url = 'horario_eliminar'
    columnas = [('dia', 'Día'), ('hora_inicio', 'Inicio'), ('hora_fin', 'Fin')]


class HorarioCreateView(BaseCreateView):
    model = Horario
    form_class = HorarioForm
    titulo = 'Horario'
    success_url = reverse_lazy('horario_lista')
    success_url_name = 'horario_lista'


class HorarioUpdateView(BaseUpdateView):
    model = Horario
    form_class = HorarioForm
    titulo = 'Horario'
    success_url = reverse_lazy('horario_lista')
    success_url_name = 'horario_lista'


class HorarioDeleteView(BaseDeleteView):
    model = Horario
    titulo = 'Horario'
    success_url = reverse_lazy('horario_lista')
    success_url_name = 'horario_lista'




class GrupoDetalleView(DetailView):
    model = Grupo
    template_name = 'escolar/grupo_detalle.html'
    context_object_name = 'grupo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo = self.object
        alumnos = []

        for estudiante in grupo.estudiantes.all().order_by('apellido_paterno', 'apellido_materno', 'nombre'):
            promedio = Calificacion.objects.filter(
                grupo=grupo,
                estudiante=estudiante
            ).aggregate(promedio=Avg('calificacion'))['promedio']

            alumnos.append({
                'numero_control': estudiante.numero_control,
                'nombre': estudiante.nombre,
                'apellido_paterno': estudiante.apellido_paterno,
                'apellido_materno': estudiante.apellido_materno,
                'promedio': promedio,
            })

        context['alumnos'] = alumnos
        return context


def grupo_pdf(request, pk):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

    grupo = get_object_or_404(
        Grupo.objects.select_related('materia', 'profesor', 'aula', 'periodo', 'horario'),
        pk=pk
    )

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="grupo_{grupo.id}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph('Reporte de Grupo', styles['Title']))
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph(f'<b>Grupo:</b> {grupo.nombre}', styles['Normal']))
    elementos.append(Paragraph(f'<b>Materia:</b> {grupo.materia}', styles['Normal']))
    elementos.append(Paragraph(f'<b>Profesor:</b> {grupo.profesor}', styles['Normal']))
    elementos.append(Paragraph(f'<b>Aula:</b> {grupo.aula}', styles['Normal']))
    elementos.append(Paragraph(f'<b>Periodo:</b> {grupo.periodo}', styles['Normal']))
    elementos.append(Spacer(1, 16))

    datos = [['No. Control', 'Nombre', 'Apellido paterno', 'Apellido materno', 'Promedio / Calificación']]

    estudiantes = grupo.estudiantes.all().order_by('apellido_paterno', 'apellido_materno', 'nombre')
    for estudiante in estudiantes:
        promedio = Calificacion.objects.filter(
            grupo=grupo,
            estudiante=estudiante
        ).aggregate(promedio=Avg('calificacion'))['promedio']

        datos.append([
            estudiante.numero_control,
            estudiante.nombre,
            estudiante.apellido_paterno,
            estudiante.apellido_materno,
            f'{promedio:.2f}' if promedio is not None else 'Sin calificación'
        ])

    if len(datos) == 1:
        datos.append(['-', 'Sin alumnos registrados', '-', '-', '-'])

    tabla = Table(datos, repeatRows=1)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#17223b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f4f6f9')]),
    ]))

    elementos.append(tabla)
    doc.build(elementos)
    return response


class GrupoListView(BaseListView):
    model = Grupo
    titulo = 'Grupos'
    crear_url = 'grupo_crear'
    editar_url = 'grupo_editar'
    eliminar_url = 'grupo_eliminar'
    detalle_url = 'grupo_detalle'
    columnas = [('nombre', 'Grupo'), ('materia', 'Materia'), ('profesor', 'Profesor'), ('aula', 'Aula'), ('periodo', 'Periodo'), ('horario', 'Horario')]


class GrupoCreateView(BaseCreateView):
    model = Grupo
    form_class = GrupoForm
    titulo = 'Grupo'
    success_url = reverse_lazy('grupo_lista')
    success_url_name = 'grupo_lista'


class GrupoUpdateView(BaseUpdateView):
    model = Grupo
    form_class = GrupoForm
    titulo = 'Grupo'
    success_url = reverse_lazy('grupo_lista')
    success_url_name = 'grupo_lista'


class GrupoDeleteView(BaseDeleteView):
    model = Grupo
    titulo = 'Grupo'
    success_url = reverse_lazy('grupo_lista')
    success_url_name = 'grupo_lista'


class CalificacionListView(BaseListView):
    model = Calificacion
    titulo = 'Calificaciones'
    crear_url = 'calificacion_crear'
    editar_url = 'calificacion_editar'
    eliminar_url = 'calificacion_eliminar'
    columnas = [('estudiante', 'Estudiante'), ('grupo', 'Grupo'), ('periodo', 'Periodo'), ('calificacion', 'Calificación'), ('observaciones', 'Observaciones')]


class CalificacionCreateView(BaseCreateView):
    model = Calificacion
    form_class = CalificacionForm
    titulo = 'Calificación'
    success_url = reverse_lazy('calificacion_lista')
    success_url_name = 'calificacion_lista'


class CalificacionUpdateView(BaseUpdateView):
    model = Calificacion
    form_class = CalificacionForm
    titulo = 'Calificación'
    success_url = reverse_lazy('calificacion_lista')
    success_url_name = 'calificacion_lista'


class CalificacionDeleteView(BaseDeleteView):
    model = Calificacion
    titulo = 'Calificación'
    success_url = reverse_lazy('calificacion_lista')
    success_url_name = 'calificacion_lista'
