from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Familiar, Curso, Estudiante, Auto
from .forms import CursoForm, EstudianteForm, AutoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.


def home(request):
    return render(request, 'mi_primer_app/home.html')


def hola_mundo(request):
    print("¡Hola, mundo!")
    return HttpResponse("¡Hola, mundo!")


def crear_familiar(request, nombre):
    if nombre is not None:
        Familiar.objects.create(
            nombre=nombre, edad=30, fecha_nacimiento="1991-01-01", parentesco="Hermano")
    return render(request, 'mi_primer_app/crear-familiar.html', {"familiar": nombre})


def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'mi_primer_app/listar-familiares.html', {"familiares": familiares})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_fin=form.cleaned_data['fecha_fin'],
                activo=form.cleaned_data['activo']
            )
            curso.save()
            return redirect('listar-cursos')

    form = CursoForm()
    return render(request, 'mi_primer_app/crear-curso.html', {"form": form})


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos, "nombre": nombre})


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
            )
            estudiante.save()
            return redirect('listar-estudiantes')

    form = EstudianteForm()
    return render(request, 'mi_primer_app/crear-estudiante.html', {"form": form})


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/listar-estudiantes.html', {"estudiantes": estudiantes})


# Vistas basadas en clases para Auto

class AutoListView(ListView):
    model = Auto
    template_name = 'mi_primer_app/listar-autos.html'
    context_object_name = 'autos'


class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear-auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear-auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'mi_primer_app/detalle-auto.html'
    context_object_name = 'auto'


class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'mi_primer_app/eliminar-auto.html'
    success_url = reverse_lazy('listar-autos')
