from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User




class Game(models.Model):

    def __str__(self) :
        return f"{self.titulo}"

    titulo= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=70)
    genero= models.CharField(max_length=30)
    fecha_de_estreno= models.DateField()
    tipo_de_juego= models.CharField(max_length=60)
    caratula= models.ImageField(upload_to = 'juegos', null=TRUE, blank=TRUE)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class Comentario(models.Model):
    comentario = models.ForeignKey( Game, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
