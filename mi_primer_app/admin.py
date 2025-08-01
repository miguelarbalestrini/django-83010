from django.contrib import admin
from .models import Familiar, Curso, Estudiante

# Register your models here.
register_models = [Familiar, Curso, Estudiante]

admin.site.register(register_models)
