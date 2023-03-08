from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.


def registro(request):
    if request.method == "POST":

        form = RegistroUsuario(request.POST)

        if form.is_valid():

            username= form.cleaned_data["username"]

            form.save()
            
            return render (request,"AppCoder/resultadoregistro.html", {"mensaje": "Usuario creado."}) 

    else: 

        form = RegistroUsuario()

    return render (request,"AppCoder/registro.html", {"formulario":form})

def resultadoregistro(request):
    return render (request,"AppCoder/resultadoregistro.html")

def iniciosesion(request):
    if request.method=="POST":

        form= AuthenticationForm(request, data= request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password= contraseña)

            if user:

                login(request,user)

                return render (request,"AppCoder/inicio.html", {"usuario": user})
            
            else:
                form = AuthenticationForm()
            
                return render (request,"AppCoder/iniciosesion.html", {"mensaje": "Datos incorrectos. Intente nuevamente.", "formulario": form}) 

    else:

       
        form = AuthenticationForm()
    return render (request,"AppCoder/iniciosesion.html", {"mensaje": "Datos incorrectos. Intente nuevamente.", "formulario": form})
    
    #return render(request, 'AppCoder/iniciosesion.html', {'formulario': form})

#+++++++++++++++++++++++++++++++++

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

    
def about(request):
    return render (request,"AppCoder/about.html")

#++++++++++++++++++++++++++++++++++++++
@login_required
def editarperfil(request):
    usuario= request.user

    if request.method == "POST":

        form= FormularioEditar(request.POST)
    
        if form.is_valid():

            info = form.cleaned_data

            usuario.username= info["username"]
            usuario.email= info ["email"]
            usuario.set_password(info["password1"])

            usuario.save()


        return render (request, "AppCoder/inicio.html")
        
    else: 
        
        form= FormularioEditar(initial={
            "email": usuario.email, 
            })
        
        contexto=  {"formulario": form, "usuario": usuario}

    return render (request, "AppCoder/editarperfil.html", contexto)
    


def buscar(request):
    return render (request,"AppCoder/busquedaGames.html")


def busquedaGame(request):


    if "tit" in request.GET:

        titulo = request.GET["tit"]

    else:

        titulo = False


    if titulo:
     
        titulo= Game.objects.filter(titulo__icontains=titulo)

        return render (request,"AppCoder/busquedaGames.html", {"titulo": titulo})

    else:

        return render(request, "AppCoder/busquedaGames.html")


class ListaJuego(LoginRequiredMixin, ListView):
    
    model= Game 


class DetalleJuego(LoginRequiredMixin, DetailView):

    model= Game

    
class CrearJuego(LoginRequiredMixin, CreateView):

    model= Game
    success_url = "/juego/list"
    fields = ["titulo", "descripcion", "genero", "fecha_de_estreno", "tipo_de_juego", "caratula"]

      
class ActualizarJuego(LoginRequiredMixin, UpdateView):

    model= Game
    success_url = "/juego/list"
    fields = ["titulo", "descripcion", "genero", "fecha_de_estreno", "tipo_de_juego", "caratula"]


class EliminarJuego(LoginRequiredMixin, DeleteView):

    model= Game
    success_url = "/juego/list"


# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppCoder/comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)



