from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Curso
from .forms import Cursoformulario
from .models import Profesor
from .forms import Profesorformulario
from .models import Estudiante
from .forms import Estudianteformulario
from .models import Entregable
from .forms import Entregableformulario

# index
def inicio(request):
    return render(request, "AppCoder/index.html")

# curso
def cursos(request):
    query = request.GET.get('q')
    if query:
        cursos = Curso.objects.filter(nombre__icontains=query)
    else:
        cursos = Curso.objects.all()

    return render(request, "AppCoder/cursos.html", {"cursos":cursos})
    
def formulario_curso_api(request):

     if request.method == "POST":
         curso_form = Cursoformulario(request.POST)

         if curso_form.is_valid():
            info_limpia = curso_form.cleaned_data
            curso = Curso(nombre=info_limpia["nombre"], camada=info_limpia["camada"])
            curso.save()
            return redirect("cursos")
     else:
            curso_form = Cursoformulario()
            contexto = {"form": curso_form}
            return render(request, "AppCoder/forms/curso_formulario.html", contexto)
     

# profesores
def profesores(request):
    
    query = request.GET.get('q')
    if query:
        profes = Profesor.objects.filter(nombre__icontains=query)
    else:
        profes = Profesor.objects.all()

    return render(request, "AppCoder/profesores.html", {"profes":profes})

def formulario_profesor(request):

     if request.method == "POST":
         form = Profesorformulario(request.POST)
         if form.is_valid():
            form.save()
            return redirect("profesores")
     else:
            form = Profesorformulario()
            return render(request, "AppCoder/forms/profesor_formulario.html", {'form':form})
     
def eliminar_profesor(request, id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return redirect("inicio")

def editar_profesor(request, id): 
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        pass
        profe_form = Profesorformulario(request.POST)
        if profe_form.is_valid():
            info_limpia = profe_form.cleaned_data
            profesor.nombre = info_limpia["nombre"]
            profesor.apellido = info_limpia["apellido"]
            profesor.email = info_limpia["email"]
            profesor.profesion = info_limpia["profesion"]
            profesor.save()
            
            return redirect("profesores")    

    else:
        profe_form = Profesorformulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})

    return render(request, "AppCoder/profesor_editar.html", {'form': profe_form})

# estudiantes
def estudiantes(request):
    
    query = request.GET.get('q')
    if query:
        alumno = Estudiante.objects.filter(nombre__icontains=query)
    else:
        alumno = Estudiante.objects.all()

    return render(request, "AppCoder/estudiantes.html", {"alumno":alumno})

def formulario_estudiante(request):

     if request.method == "POST":
         form = Estudianteformulario(request.POST)
         if form.is_valid():
            form.save()
            return redirect("estudiantes")
     else:
            form = Estudianteformulario()
            return render(request, "AppCoder/forms/estudiante_formulario.html", {'form':form})
     
def eliminar_estudiante(request, id):
    
    alumno = Estudiante.objects.get(id=id)
    alumno.delete()
    return redirect("estudiantes")

def editar_estudiante(request, id): 
    alumno = Estudiante.objects.get(id=id)

    if request.method == "POST":
        pass
        alumno_form = Estudianteformulario(request.POST)
        if alumno_form.is_valid():
            info_limpia = alumno_form.cleaned_data
            alumno.nombre = info_limpia["nombre"]
            alumno.apellido = info_limpia["apellido"]
            alumno.email = info_limpia["email"]
            alumno.profesion = info_limpia["profesion"]
            alumno.save()
            
            return redirect("estudiantes")    

    else:
        alumno_form = Estudianteformulario(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido, 'email': alumno.email, 'profesion': alumno.profesion})

    return render(request, "AppCoder/estudiante_editar.html", {'form': alumno_form})


# entregables
def entregables(request):
    
    query = request.GET.get('q')
    if query:
        entregar = Entregable.objects.filter(nombre__icontains=query)
    else:
        entregar = Entregable.objects.all()

    return render(request, "AppCoder/entregables.html", {"entregar":entregar})

def formulario_entregables(request):

     if request.method == "POST":
         form = Entregableformulario(request.POST)
         if form.is_valid():
            form.save()
            return redirect("entregables")
     else:
            form = Entregableformulario()
            return render(request, "AppCoder/forms/entregable_formulario.html", {'form':form})
     
def eliminar_entregables(request, id):
    
    entregar = Entregable.objects.get(id=id)
    entregar.delete()
    return redirect("entregables")

def editar_entregables(request, id): 
    entregar = Entregable.objects.get(id=id)

    if request.method == "POST":
        pass
        entregar_form = Entregableformulario(request.POST)
        if entregar_form.is_valid():
            info_limpia = entregar_form.cleaned_data
            entregar.nombre = info_limpia["nombre"]
            entregar.apellido = info_limpia["apellido"]
            entregar.email = info_limpia["email"]
            entregar.profesion = info_limpia["profesion"]
            entregar.save()
            
            return redirect("entregables")    

    else:
        alumno_form = Entregableformulario(initial={'nombre': entregar.nombre, 'apellido': entregar.apellido, 'email': entregar.email, 'profesion': entregar.profesion})

    return render(request, "AppCoder/entregables_editar.html", {'form': entregar_form})


