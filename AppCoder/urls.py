from django.urls import path
from .views import *
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from .urls import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('iniciosesion/',iniciosesion, name='iniciosesion'),
    path('registro/',registro, name='registro'),
    path('editarperfil/',editarperfil, name='editarperfil'),
    path('resultadoregistro/', resultadoregistro, name="resultadoregistro"),
    path("busquedagame/", busquedaGame, name= "busquedagame"),
    path("buscar/", buscar, name = "buscar"),
    path("about/",about, name = "about"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name= "logout"),

    
    #Vistas Clases

    path("juego/list/", ListaJuego.as_view(), name="ListaGame"),
    path("juego/crear/", CrearJuego.as_view(), name="CrearGame"),
    path("detalle/<int:pk>", DetalleJuego.as_view(), name="DetalleGame"),
    path("juego/actualizar/<int:pk>", ActualizarJuego.as_view(), name="ActualizarGame"),
    path("juego/eliminar<int:pk>", EliminarJuego.as_view(), name="EliminarGame"),
    #Comentario
    path('gameDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    
] 

