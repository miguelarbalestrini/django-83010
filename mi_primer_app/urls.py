from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hola-mundo/', views.hola_mundo, name='hola-mundo'),
    path('crear-familiar/<str:nombre>/',
         views.crear_familiar, name='crear-familiar'),
    path('listar-familiares/', views.listar_familiares, name="listar-familiares"),
    path('crear-curso/',
         views.crear_curso, name='crear-curso'),
    path('listar-cursos/', views.listar_cursos, name="listar-cursos"),
    path('cursos/buscar', views.buscar_cursos, name="buscar-cursos"),
    path('crear-estudiante/',
         views.crear_estudiante, name='crear-estudiante'),
    path('listar-estudiantes/', views.listar_estudiantes,
         name="listar-estudiantes"),


    # Vistas basadas en clases
    path('crear-auto/', views.AutoCreateView.as_view(), name="crear-auto"),
    path('listar-autos/', views.AutoListView.as_view(), name="listar-autos"),
    path('detalle-auto/<int:pk>/',
         views.AutoDetailView.as_view(), name="detalle-auto"),
    path('editar/<int:pk>/', views.AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar/<int:pk>/', views.AutoDeleteView.as_view(), name='eliminar-auto'),

]
