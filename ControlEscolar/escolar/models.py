from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Carrera(models.Model):
    nombre = models.CharField(max_length=120)
    clave = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80, blank=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    especialidad = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"


class Estudiante(models.Model):
    numero_control = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80, blank=True)
    correo = models.EmailField(unique=True)
    semestre = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT, related_name='estudiantes')

    def __str__(self):
        return f"{self.numero_control} - {self.nombre} {self.apellido_paterno}"


class Materia(models.Model):
    clave = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120)
    creditos = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(20)])
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT, related_name='materias')

    def __str__(self):
        return f"{self.clave} - {self.nombre}"


class Aula(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    capacidad = models.PositiveIntegerField(default=30)
    ubicacion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre


class PeriodoSemestral(models.Model):
    nombre = models.CharField(max_length=80)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
    ]

    dia = models.CharField(max_length=20, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.dia} {self.hora_inicio} - {self.hora_fin}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT, related_name='grupos')
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT, related_name='grupos')
    aula = models.ForeignKey(Aula, on_delete=models.PROTECT, related_name='grupos')
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.PROTECT, related_name='grupos')
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT, related_name='grupos')
    estudiantes = models.ManyToManyField(Estudiante, blank=True, related_name='grupos')

    def __str__(self):
        return f"{self.nombre} - {self.materia.nombre}"


class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificaciones')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='calificaciones')
    periodo = models.ForeignKey(PeriodoSemestral, on_delete=models.PROTECT, related_name='calificaciones')
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    observaciones = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('estudiante', 'grupo', 'periodo')

    def __str__(self):
        return f"{self.estudiante} - {self.grupo}: {self.calificacion}"
