from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Game, Comentario

class Juegosingreso(forms.ModelForm):

    class Meta:
        
        model= Game
        fields=  ["titulo", "descripcion", "genero", "fecha_de_estreno", "tipo_de_juego", "caratula"]

        
class RegistroUsuario(UserCreationForm):
    username = forms.CharField()
    email= forms.EmailField()
    password1= forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]

        
class FormularioEditar(UserCreationForm):

    username = forms.CharField()
    email= forms.EmailField()
    password1= forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label= "Repita su contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"] 


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }