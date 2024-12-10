from django.db import models

# Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    camada = models.IntegerField() 
    

    def __str__(self):
        return f"Nombre del curso: {self.nombre} - Numero de camada: {self.camada}"

# Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 30 caracteres
    email = models.EmailField()  # Campo de email
    profesion = models.CharField(max_length=50)  # Campo string de 50 caracteres

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Profesion: {self.profesion} - E-mail: {self.email}"
    
# Estudiante
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 100 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 100 caracteres
    email = models.EmailField()  # Campo de email 

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-mail: {self.email}"

# Entregable    
class Entregable(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    fechaDeEntrega = models.DateField()  # Campo de fecha
    entregado = models.BooleanField()  # Campo booleano

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha limite: {self.fechaDeEntrega} - Entregado: {self.entregado}"