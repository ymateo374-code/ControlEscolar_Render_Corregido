from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('carreras/', views.CarreraListView.as_view(), name='carrera_lista'),
    path('carreras/nuevo/', views.CarreraCreateView.as_view(), name='carrera_crear'),
    path('carreras/<int:pk>/editar/', views.CarreraUpdateView.as_view(), name='carrera_editar'),
    path('carreras/<int:pk>/eliminar/', views.CarreraDeleteView.as_view(), name='carrera_eliminar'),

    path('profesores/', views.ProfesorListView.as_view(), name='profesor_lista'),
    path('profesores/nuevo/', views.ProfesorCreateView.as_view(), name='profesor_crear'),
    path('profesores/<int:pk>/editar/', views.ProfesorUpdateView.as_view(), name='profesor_editar'),
    path('profesores/<int:pk>/eliminar/', views.ProfesorDeleteView.as_view(), name='profesor_eliminar'),

    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiante_lista'),
    path('estudiantes/nuevo/', views.EstudianteCreateView.as_view(), name='estudiante_crear'),
    path('estudiantes/<int:pk>/editar/', views.EstudianteUpdateView.as_view(), name='estudiante_editar'),
    path('estudiantes/<int:pk>/eliminar/', views.EstudianteDeleteView.as_view(), name='estudiante_eliminar'),

    path('materias/', views.MateriaListView.as_view(), name='materia_lista'),
    path('materias/nuevo/', views.MateriaCreateView.as_view(), name='materia_crear'),
    path('materias/<int:pk>/editar/', views.MateriaUpdateView.as_view(), name='materia_editar'),
    path('materias/<int:pk>/eliminar/', views.MateriaDeleteView.as_view(), name='materia_eliminar'),

    path('aulas/', views.AulaListView.as_view(), name='aula_lista'),
    path('aulas/nuevo/', views.AulaCreateView.as_view(), name='aula_crear'),
    path('aulas/<int:pk>/editar/', views.AulaUpdateView.as_view(), name='aula_editar'),
    path('aulas/<int:pk>/eliminar/', views.AulaDeleteView.as_view(), name='aula_eliminar'),

    path('periodos/', views.PeriodoListView.as_view(), name='periodo_lista'),
    path('periodos/nuevo/', views.PeriodoCreateView.as_view(), name='periodo_crear'),
    path('periodos/<int:pk>/editar/', views.PeriodoUpdateView.as_view(), name='periodo_editar'),
    path('periodos/<int:pk>/eliminar/', views.PeriodoDeleteView.as_view(), name='periodo_eliminar'),

    path('horarios/', views.HorarioListView.as_view(), name='horario_lista'),
    path('horarios/nuevo/', views.HorarioCreateView.as_view(), name='horario_crear'),
    path('horarios/<int:pk>/editar/', views.HorarioUpdateView.as_view(), name='horario_editar'),
    path('horarios/<int:pk>/eliminar/', views.HorarioDeleteView.as_view(), name='horario_eliminar'),

    path('grupos/', views.GrupoListView.as_view(), name='grupo_lista'),
    path('grupos/nuevo/', views.GrupoCreateView.as_view(), name='grupo_crear'),
    path('grupos/<int:pk>/editar/', views.GrupoUpdateView.as_view(), name='grupo_editar'),
    path('grupos/<int:pk>/eliminar/', views.GrupoDeleteView.as_view(), name='grupo_eliminar'),

    path('calificaciones/', views.CalificacionListView.as_view(), name='calificacion_lista'),
    path('calificaciones/nuevo/', views.CalificacionCreateView.as_view(), name='calificacion_crear'),
    path('calificaciones/<int:pk>/editar/', views.CalificacionUpdateView.as_view(), name='calificacion_editar'),
    path('calificaciones/<int:pk>/eliminar/', views.CalificacionDeleteView.as_view(), name='calificacion_eliminar'),
]
