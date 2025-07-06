from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField(blank=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Educacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='educaciones')
    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    nivel = models.CharField(max_length=100, blank=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.institucion} - {self.titulo}"

class Experiencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='experiencias')
    empresa = models.CharField(max_length=200)
    puesto = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.empresa} - {self.puesto}"

class Habilidad(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='habilidades')
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)  # 1-5
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria}"

class Tecnologia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tecnologias')
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)  # Frameworks, Bases de datos, etc.
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria}"