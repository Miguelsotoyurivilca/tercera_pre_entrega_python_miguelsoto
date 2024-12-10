from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('entregables', views.entregables, name="entregables"),
   
    #curso
    
    path('curso_formulario', views.formulario_curso_api, name="curso_formulario"),
    
    #profesor

    path('profesor_formulario', views.formulario_profesor, name="profesor_formulario"),

    path('profe_eliminar/<int:id>', views.eliminar_profesor, name="profe_eliminar"),

    path('profe_editar/<int:id>', views.editar_profesor, name="profe_editar"),

    #estudiante

    path('estudiante_formulario', views.formulario_estudiante, name="estudiante_formulario"),

    path('estudiante_eliminar/<int:id>', views.eliminar_estudiante, name="estudiante_eliminar"),

    path('estudiante_editar/<int:id>', views.editar_estudiante, name="estudiante_editar"),

    #entregables

    path('entregable_formulario', views.formulario_entregables, name="entregable_formulario"),

    path('entregable_eliminar/<int:id>', views.eliminar_entregables, name="entregable_eliminar"),

    path('entregable_editar/<int:id>', views.editar_entregables, name="entregable_editar"),
]

